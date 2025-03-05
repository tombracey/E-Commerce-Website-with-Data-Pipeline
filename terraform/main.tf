provider "aws" {
  region = "eu-west-2"
}

resource "aws_iam_policy" "s3_create_bucket_policy" {
  name = "S3CreateBucketPolicy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "s3:CreateBucket",
          "s3:PutBucketTagging"
        ]
        Resource = [
          "arn:aws:s3:::*",
          "arn:aws:s3:::*/*"
        ]
      }
    ]
  })
}

resource "aws_iam_user_policy_attachment" "user_policy_attachment" {
  user       = "tombracey"
  policy_arn = aws_iam_policy.s3_create_bucket_policy.arn
}

resource "aws_s3_bucket" "ingestion_bucket" {
  bucket = "oud-ingestion-bucket"

  tags = {
    Name = "ingestion bucket"
  }

  depends_on = [aws_iam_user_policy_attachment.user_policy_attachment]
}