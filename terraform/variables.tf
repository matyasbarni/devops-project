variable "namespace" {
  description = "Kubernetes namespace for the homework deployment"
  type        = string
  default     = "production"
}

variable "environment" {
  description = "Environment value passed to the Helm chart"
  type        = string
  default     = "prod"
}

variable "image_tag" {
  description = "Container image tag to deploy"
  type        = string
  default     = "latest"
}