# cloud-devops-cicd-platform
# Production-Style DevOps CI/CD Cloud Deployment Platform

## Overview

This project demonstrates a production-style DevOps deployment workflow using Docker, Terraform, GitHub Actions, AWS, and Azure.

The same containerized web application is deployed to both AWS and Azure using Infrastructure as Code and automated CI/CD pipelines.

## Technologies Used

- Python Flask
- Docker
- GitHub Actions
- Terraform
- AWS ECS Fargate
- Amazon ECR
- AWS Application Load Balancer
- AWS CloudWatch
- Azure App Service
- Azure Container Registry
- Azure Monitor
- Application Insights

## Architecture

### AWS

GitHub → GitHub Actions → Docker Build → Amazon ECR → ECS Fargate → Application Load Balancer → CloudWatch Logs

### Azure

GitHub → GitHub Actions → Docker Build → Azure Container Registry → Azure App Service → Azure Monitor

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Web homepage |
| `/health` | Health check endpoint |
| `/version` | Application version endpoint |

## DevOps Skills Demonstrated

- CI/CD pipeline automation
- Docker image creation
- Cloud container deployment
- Infrastructure as Code using Terraform
- Environment-specific deployment
- Cloud logging and monitoring
- Health checks
- Deployment validation
- Production-style troubleshooting documentation

## Local Run

```bash
cd app
docker build -t cloud-devops-app .
docker run -p 5000:5000 cloud-devops-app
