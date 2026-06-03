variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Project name. Use lowercase letters and numbers only for safer Azure naming."
  type        = string
  default     = "azdevopsca"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "container_image" {
  description = "Initial container image"
  type        = string
  default     = "mcr.microsoft.com/k8se/quickstart:latest"
}