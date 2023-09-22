locals{
  name = "complete-postgresql"
  vpc_cidr = "10.0.0.0/16"
}
# VPC for ECS Fargate
data "aws_availability_zones" "available" {}

module "vpc_for_ecs_fargate" {
  source = "./vpc"
  vpc_tag_name = "${var.platform_name}-vpc"
  number_of_private_subnets = 2
  private_subnet_tag_name = "${var.platform_name}-private-subnet"
  # route_table_tag_name = "${var.platform_name}-rt"
  environment = var.environment
  security_group_lb_name = "${var.platform_name}-alb-sg"
  security_group_ecs_tasks_name = "${var.platform_name}-ecs-tasks-sg"
  app_port = var.app_port
  # main_pvt_route_table_id = var.main_pvt_route_table_id
  availability_zones = var.availability_zones
  region = var.region
}

# ECS cluster
module ecs_cluster {
  source = "./ecs-cluster"
  name = "${var.platform_name}-${var.environment}-cluster"
  cluster_tag_name = "${var.platform_name}-${var.environment}-cluster"
}

# ECS task definition and service
module ecs_task_definition_and_service {
  # Task definition and NLB
  source = "./ecs-fargate"
  name = "${var.platform_name}-${var.environment}"
  app_image = var.app_image
  fargate_cpu                 = 256
  fargate_memory              = 512
  app_port = var.app_port
  vpc_id = module.vpc_for_ecs_fargate.vpc_id
  environment = var.environment
  # Service
  cluster_id = module.ecs_cluster.id 
  app_count = var.app_count
  aws_security_group_ecs_tasks_id = module.vpc_for_ecs_fargate.ecs_tasks_security_group_id
  private_subnet_ids = module.vpc_for_ecs_fargate.private_subnet_ids
}

# API Gateway and VPC link
module api_gateway {
  source = "./api-gateway"
  name = "${var.platform_name}-${var.environment}"
  integration_input_type = "HTTP_PROXY"
  path_part = "{proxy+}"
  app_port = var.app_port
  nlb_dns_name = module.ecs_task_definition_and_service.nlb_dns_name
  nlb_arn = module.ecs_task_definition_and_service.nlb_arn
  environment = var.environment
}

resource "aws_security_group" "pg" {
  name        = "${var.security_group_pg_name}-${var.environment}"
  description = "${var.security_group_pg_description}"
  vpc_id      = module.vpc_for_ecs_fargate.vpc_id

  ingress {
    protocol  = "-1"
    self      = true
    from_port = 0
    to_port   = 0
  }

  ingress {
    protocol    = "tcp"
    from_port   = 5432
    to_port     = 5432
    cidr_blocks = [local.vpc_cidr] #["0.0.0.0/0"]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 5432
    to_port     = 5432
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_db_subnet_group" "postgres" {
  name            = "${var.platform_name}-${var.environment}-pg"
  subnet_ids      = module.vpc_for_ecs_fargate.private_subnet_ids
  tags = {
    Name = "postgres_subnet"
  }
}
resource "aws_db_parameter_group" "postgres" {
  name   = "${var.platform_name}-${var.environment}-pg"
  family = "postgres14"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "aws_s3_bucket" "s3" {
  bucket = "s3-bucket-${local.name}"
  acl    = "private"

  tags = {
    Name        = "S3 Bucket with init.sql dump"
    Environment = local.name
  }
}

resource "aws_s3_object" "init_sql" {
  bucket = aws_s3_bucket.s3.id
  key    = "init.sql.tar.gz"
  source = "${path.module}/init.sql.tar.gz"
} 

/* data "aws_db_snapshot" "db_snapshot" {
    most_recent = true
    db_instance_identifier = "data-coe-gsa-aurorapg-sampledata-snapshot-1"
}*/

/* resource "aws_db_instance" "postgres" {
  identifier             = "postgres"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "14.9"
  username               = "gsa_data_pguser"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.postgres.name
  vpc_security_group_ids = [aws_security_group.pg.id]
  parameter_group_name   = aws_db_parameter_group.postgres.name
  snapshot_identifier    = "rds:data-coe-gsa-aurorapg-sampledata-snapshot-1" //"${data.aws_db_snapshot.db_snapshot.id}"
  publicly_accessible    = false
  skip_final_snapshot    = true
} */

data "aws_db_cluster_snapshot" "snapshot" {
  db_cluster_identifier = "data-coe-gsa-aurorapg-sampledata"
  most_recent = true
}
resource "aws_rds_cluster" "sandbox" {
  cluster_identifier  = "aurora-postgres-cluster-${local.name}"
  engine              = "aurora-postgresql"
  engine_version      = "13.8"
  port                = var.db_port
  availability_zones  = slice(data.aws_availability_zones.available.names, 0, 2)
  master_username     = var.db_user
  master_password     = var.db_password
  skip_final_snapshot = true
  apply_immediately   = true
  snapshot_identifier = "${data.aws_db_cluster_snapshot.snapshot.id}"
  vpc_security_group_ids = [aws_security_group.pg.id]
  db_subnet_group_name = aws_db_subnet_group.postgres.name
  db_instance_parameter_group_name = aws_db_parameter_group.postgres.name
  lifecycle {
    ignore_changes = [engine_version]
  }

  depends_on = [
    aws_db_subnet_group.postgres,
    aws_security_group.pg,
  ]
}

resource "aws_rds_cluster_instance" "cluster_instance" {
  count              = 1
  identifier         = "aurora-cluster-instance-${count.index}"
  cluster_identifier = aws_rds_cluster.sandbox.id
  instance_class     = "db.t4g.large"
  engine             = aws_rds_cluster.sandbox.engine
  engine_version     = aws_rds_cluster.sandbox.engine_version

  lifecycle {
    ignore_changes = [engine_version]
  }
}
