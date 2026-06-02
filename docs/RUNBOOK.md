Runbook Documentation

Create:

## `docs/runbook.md`

# Production Support Runbook

## Application Name

Cloud DevOps CI/CD Platform

## Common Health Check

```bash
curl https://APPLICATION_URL/health


Expected result:
{
  "status": "healthy"
}

AWS Troubleshooting
Check ECS Service
aws ecs describe-services \
  --cluster cloud-devops-cicd-platform-cluster \
  --services cloud-devops-cicd-platform-service \
  --region us-east-1

( aws ecs describe-services --cluster cloud-devops-cicd-platform-cluster --services cloud-devops-cicd-platform-service --region us-east-1 )

Check CloudWatch Logs
Go to: CloudWatch → Log Groups → /ecs/cloud-devops-cicd-platform

Force ECS Redeployment
aws ecs update-service \
  --cluster cloud-devops-cicd-platform-cluster \
  --service cloud-devops-cicd-platform-service \
  --force-new-deployment \
  --region us-east-1

( aws ecs update-service --cluster cloud-devops-cicd-platform-cluster --service cloud-devops-cicd-platform-service --force-new-deployment --region us-east-1 )


Azure Troubleshooting
Check Web App Status
az webapp show \
  --name clouddevopscicd-dev-app \
  --resource-group clouddevopscicd-dev-rg \
  --query state

Restart Web App
az webapp restart \
  --name clouddevopscicd-dev-app \
  --resource-group clouddevopscicd-dev-rg

View Logs
az webapp log tail \
  --name clouddevopscicd-dev-app \
  --resource-group clouddevopscicd-dev-rg

Rollback Plan
Identify previous working Docker image tag.
Retag previous image as latest.
Push image to registry.
Restart ECS service or Azure Web App.
Validate /health endpoint.

