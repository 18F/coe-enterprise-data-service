# Deploy Container in ECS Fargate behind API Gateway & NLB for Secure Optimal Accessibility (with Terraform)
## Overview
This repository contains the source code for a containerised application in AWS ECS Fargate inside a VPC's private subnets. An API Gateway is used as the doorway to the private network using a VPC link to access the VPC. An NLB is for optimal performance of accessing the application running in the private subnets. This also creates database from the snapshots and creates a postgres db server.  The whole setup is secured using cognito.

## Prerequisites:
    1. Install and configure AWS Cli 
    2. Install Visual Studio Code and enable Git
    3. Install Python 3.11 or higher
    3. Install terraform.  Visit, https://www.terraform.io/
    4. Install terragrunt.  For quick info, visit https://terragrunt.gruntwork.io/docs/getting-started/quick-start/
    5. Install docker.  For docs, visit https://docs.docker.com/engine/install/

## To create the infrastructure

terragrunt apply --auto-approve

## To destroy the infrastructure

terragrunt destroy --auto-approve

## Create user in congnito (after stack runs without error)
-->go to aws console-->search/select "cognito" --> select the user pool "eds_user_pool" and create a username and password

# to Enable Access Token
aws cognito-idp admin-set-user-password \
     --user-pool-id ${user_pool_id} \
     --username ${username} \
     --password ${password} \
     --permanent
# To get the Access token
aws cognito-idp initiate-auth \
 --client-id ${client_d} \
 --auth-flow USER_PASSWORD_AUTH \
 --auth-parameters USERNAME=${username},PASSWORD=${password} \
 --query 'AuthenticationResult.IdToken' \
 --output text

# To use the EndPoint
# Run the GET endpoint from the API Gateway/Stage 
curl -H "Authorization: ${TOKEN}" https://${API_URL}/dev-env/hello

## Incase, if you needed to build container image and push it to registry
## update the account and region on the following commands and execute
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <<account-number>>.dkr.ecr.<<region>>.amazonaws.com
docker build -t eds-ecr-demo-repo .
docker tag eds-ecr-demo-repo:latest <<account-number>>.dkr.ecr.<<region>>.amazonaws.com/eds-ecr-demo-repo:latest
docker push <<account-number>>.dkr.ecr.<<region>>.amazonaws.com/eds-ecr-demo-repo:latest
