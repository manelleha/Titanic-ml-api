provider "azurerm" {
  features {}
  subscription_id = "7ff17116-ebf5-46ca-8879-e9bb1349b268"
}

resource "azurerm_resource_group" "main" {
  name     = "rg-titanic-ml"
  location = "uksouth"
}

resource "azurerm_container_registry" "acr" {
  name                = "titanicmlacr${substr(uuid(),0,8)}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_app_service_plan" "appsp" {
  name                = "titanic-ml-plan"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  kind                = "Linux"   # ← CORRECTION
  reserved            = true      # ← CORRECTION
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "webapp" {
  name                = "titanic-ml-api-app${substr(uuid(),0,6)}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.appsp.id

  site_config {
    linux_fx_version = "DOCKER|${azurerm_container_registry.acr.login_server}/titanic-api:latest"
    always_on        = true
  }

  app_settings = {
    "WEBSITES_PORT"                  = "80"
    "DOCKER_REGISTRY_SERVER_URL"      = "https://${azurerm_container_registry.acr.login_server}"
    "DOCKER_REGISTRY_SERVER_USERNAME" = azurerm_container_registry.acr.admin_username
    "DOCKER_REGISTRY_SERVER_PASSWORD" = azurerm_container_registry.acr.admin_password
  }
}