provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_compute_network" "vpc_network" {
  name = "indimorph-network"
}

resource "google_compute_instance" "backend" {
  name         = "indimorph-backend"
  machine_type = "e2-medium"
  zone         = var.zone
  boot_disk {
    initialize_params {
      image = var.image
    }
  }
  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {}
  }
  metadata_startup_script = file("../../scripts/setup_env.sh")
}

resource "google_storage_bucket" "results" {
  name     = var.gcs_bucket
  location = var.region
}

variable "project_id" {}
variable "region" { default = "us-central1" }
variable "zone" { default = "us-central1-a" }
variable "image" {}
variable "gcs_bucket" {} 