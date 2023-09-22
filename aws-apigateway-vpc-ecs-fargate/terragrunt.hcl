generate "provider" {
  path = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
  provider "aws" {
     region  = "us-east-2"
     profile = "default"
  }
  terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
}
  required_version = "~> 1.5.3"
  backend "s3" {}
  }
EOF
}

remote_state {
  backend = "s3"
  config = {
    encrypt                 = true
    bucket                  = "eds-gsa-http-api-terraform-state"  #change the bucket name here
    key                     = "${path_relative_to_include()}/terraform.tfstate"
    dynamodb_table          = "eds-lock-table"
    profile                 = "default"
    region                  = "us-east-2"
  }
}