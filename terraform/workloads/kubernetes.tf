terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.74.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.1"
    }
  }
}

data "terraform_remote_state" "gke" {
  backend = "local"

  config = {
    path = "../clusters/terraform.tfstate"
  }
}

# Retrieve GKE cluster information
provider "google" {
  project = data.terraform_remote_state.gke.outputs.project_id
  region  = data.terraform_remote_state.gke.outputs.region
  zone  = data.terraform_remote_state.gke.outputs.zone
}

# Configure kubernetes provider with Oauth2 access token.
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_config
# This fetches a new token, which will expire in 1 hour.
data "google_client_config" "default" {}

data "google_container_cluster" "my_cluster" {
  name     = data.terraform_remote_state.gke.outputs.kubernetes_cluster_name
  location = data.terraform_remote_state.gke.outputs.zone
}

provider "kubernetes" {
  host = data.terraform_remote_state.gke.outputs.kubernetes_cluster_host

  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(data.google_container_cluster.my_cluster.master_auth[0].cluster_ca_certificate)
}


resource "kubernetes_deployment" "maintainly-prod" {
  metadata {
    name = "maintainly-prod"
    labels = {
      App = "maintainly"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "maintainly"
      }
    }
    template {
      metadata {
        labels = {
          App = "maintainly"
        }
      }
      spec {
        container {
          image = "us-east1-docker.pkg.dev/maintainly-prod/maintainly-dockerhub/maintainly_amd@sha256:4df1283e698e14056abf4c764a7e3e38a43bca25c3cf5de737625560f1f519a5"
          name  = "maintainly-app"

          port {
            container_port = 8000
          }

          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}
