# Create a new Web Droplet in the nyc2 region\
data "digitalocean_project" "terraform" {
  name = "Terraform VPC"
}

resource "digitalocean_droplet" "web" {
  image   = "ubuntu-20-04-x64"
  name    = "web-1"
  region  = "nyc2"
  size    = "s-1vcpu-1gb"
}

resource "digitalocean_project_resources" "terraform" {
  project = data.digitalocean_project.terraform.id
  resources = [
    digitalocean_droplet.web.urn
  ]
}