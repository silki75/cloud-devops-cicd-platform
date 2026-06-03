output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "container_app_name" {
  value = azurerm_container_app.app.name
}

output "container_app_url" {
  value = "https://${azurerm_container_app.app.latest_revision_fqdn}"
}

output "log_analytics_workspace_name" {
  value = azurerm_log_analytics_workspace.main.name
}