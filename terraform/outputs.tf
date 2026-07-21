output "namespace" {
  description = "The namespace created for the application"
  value       = kubernetes_namespace.homework.metadata[0].name
}

output "release_name" {
  description = "The Helm release name"
  value       = helm_release.homework.name
}
