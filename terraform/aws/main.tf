provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_security_group" "indimorph_sg" {
  vpc_id = aws_vpc.main.id
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "backend" {
  ami           = var.ami_id
  instance_type = "t3.medium"
  subnet_id     = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.indimorph_sg.id]
  user_data     = file("../../scripts/setup_env.sh")
  tags = { Name = "IndiMorph-Backend" }
}

resource "aws_s3_bucket" "results" {
  bucket = var.s3_bucket
  acl    = "private"
}

resource "aws_ecr_repository" "indimorph" {
  name = "indimorph"
}

variable "aws_region" { default = "us-east-1" }
variable "ami_id" {}
variable "s3_bucket" {} 