variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  default     = "cloud-devops-cicd-platform"
}

variable "container_port" {
  description = "Application container port"
  default     = 5000
}