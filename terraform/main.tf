provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "ingestion-bucket" {
  bucket = "oud-ingestion-bucket"

  tags = {
    Name        = "ingestion bucket"
  }
}