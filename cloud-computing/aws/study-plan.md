# ☁️ AWS Study To-Do List

> Goal: Learn the core AWS services relevant to data engineering and build confidence to deploy and manage data pipelines in the cloud.

## 🔹 1. Foundations of AWS
- [ ] Understand the AWS global infrastructure (Regions, AZs, Edge Locations)
- [ ] Explore the AWS Free Tier and create a free account
- [ ] Learn the shared responsibility model
- [ ] Introduction to the AWS Management Console and AWS CLI
- [ ] Set up IAM user and CLI credentials securely
- [ ] Understand pricing, billing, and the AWS calculator


## 🔹 2. Identity and Access Management (IAM)
- [ ] Create IAM users, groups, roles, and policies
- [ ] Understand the principle of least privilege
- [ ] Explore service-linked roles and temporary credentials
- [ ] Learn about IAM roles for EC2 and Lambda
- [ ] Use AWS managed vs. custom policies


## 🔹 3. Compute: EC2 + Lambda Basics

### EC2 (Elastic Compute Cloud)
- [ ] Launch a Linux EC2 instance and SSH into it
- [ ] Attach and use EBS volumes
- [ ] Create custom AMIs and understand instance lifecycle
- [ ] Set up basic monitoring with CloudWatch

### Lambda
- [ ] Understand serverless computing model
- [ ] Create a Lambda function (Python preferred)
- [ ] Trigger with S3 or API Gateway
- [ ] Monitor with CloudWatch Logs


## 🔹 4. Storage: Amazon S3
- [ ] Understand buckets, objects, and prefixes (folder structure)
- [ ] Upload/download files using CLI and Boto3 (Python SDK)
- [ ] Use lifecycle rules (archival, expiration)
- [ ] Learn about storage classes (Standard, Intelligent-Tiering, Glacier)
- [ ] Apply bucket policies and IAM policies
- [ ] Enable versioning and encryption
- [ ] Configure static website hosting with S3


## 🔹 5. Monitoring and Logging
- [ ] Explore CloudWatch metrics and custom dashboards
- [ ] Set up alarms (e.g., EC2 CPU usage)
- [ ] Use CloudWatch Logs for Lambda, EC2, etc.
- [ ] Understand AWS CloudTrail (audit/log AWS API calls)
- [ ] Set up log retention and log groups


## 🔹 6. Networking Basics (VPC)
- [ ] Understand what a VPC is (Virtual Private Cloud)
- [ ] Configure subnets, route tables, and internet gateways
- [ ] Use security groups and network ACLs
- [ ] Set up a public and private subnet setup
- [ ] Connect EC2 inside a VPC


## 🔹 7. Data Engineer Essentials

> Services you’ll touch often when building pipelines

- [ ] Launch a simple data pipeline using:
  - [ ] S3 → Lambda → S3
  - [ ] S3 → EC2 (Spark job) → Save result back to S3
- [ ] Use AWS Glue (basic ETL + crawler)
- [ ] Explore Athena for querying Parquet files in S3
- [ ] Try setting up a basic EMR cluster (with Spark)


## 🔹 8. Security and Best Practices
- [ ] Enable MFA for root and IAM users
- [ ] Set up billing alerts
- [ ] Apply IAM access analyzer to detect public resources
- [ ] Use parameter store or secrets manager for credentials
- [ ] Set up secure logging and encryption defaults

## 🔹 9. Optional: Prepare for AWS Cloud Practitioner (Cert Path)
- [ ] Follow the Cloud Practitioner Essentials course (AWS Skill Builder)
- [ ] Review whitepapers:
  - [ ] Well-Architected Framework
  - [ ] Security Best Practices


> ✅ Progressively mark the checkboxes as you complete each topic. Happy learning!
