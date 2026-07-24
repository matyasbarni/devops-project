variable "namespace" {
  description = "Kubernetes namespace for the homework deployment"
  type        = string
  default     = "demo"
}

variable "environment" {
  description = "The environment for the deployment (e.g. dev, test, stage, prod)"
  type        = string
  default     = "dev"
}

variable "image_tag" {
  description = "The tag of the Docker image to deploy"
  type        = string
  default     = "1234"
}