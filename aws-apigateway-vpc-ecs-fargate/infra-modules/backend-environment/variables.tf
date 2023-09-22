variable "module" {
  description = "The terraform module used to deploy"
  type        = string
}

variable "profile" {
  description = "AWS profile"
  type        = string
  default     = "default"
}

variable "region" {
  description = "aws region to deploy to"
  type        = string
  default = "us-east-2"
}

variable "platform_name" {
  description = "The name of the platform"
  type = string
  default="eds-nodejs"
}

variable "environment" {
  description = "Applicaiton environment"
  type = string
  default="eds-nodejs"
}

variable "app_port" {
  description = "Application port"
  type = number
  default=80
}

variable "app_image" {
  type = string 
  description = "Container image to be used for application in task definition file"
  default="533787958253.dkr.ecr.us-east-2.amazonaws.com/eds-ecr-demo-repo:latest"
}

variable "availability_zones" {
  type  = list(string)
  description = "List of availability zones for the selected region"
  default = ["us-east-2a", "us-east-2b", "us-east-2c"]
}

variable "app_count" {
  type = string 
  description = "The number of instances of the task definition to place and keep running."
  default = 3
}

/* variable "main_pvt_route_table_id" {
  type        = string
  description = "Main route table id"
} */

variable "db_password" {
  description = "RDS root user password"
  type        = string
  sensitive   = true
  default     = "dqVvAy89h9RsV3kEKn"
}
variable "db_user" {
  description = "RDS root user name"
  type        = string
  sensitive   = true
  default     = "gsa_data_pguser"
}

variable "db_port" {
  description = "RDS PG Port"
  type        = number
  default     = 5432
}
variable "security_group_pg_name" {
  type        = string
  default     = "pg-sg"
  description = "Postgres security group name"
}

variable "security_group_pg_description" {
  type        = string
  default     = "controls access to the Postgres"
  description = "Postgres security group description"
}
 