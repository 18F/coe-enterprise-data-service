resource "aws_iam_role" "s3_rds" {
  name_prefix = "rds-s3-integration-role-"

  assume_role_policy = <<EOF
{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": [
              "rds.amazonaws.com",
              "export.rds.amazonaws.com"
            ]
          },
         "Action": "sts:AssumeRole"
       }
     ]
   }
EOF
}

resource "aws_iam_role_policy" "s3_rds" {
  name_prefix = "rds-s3-integration-policy-"
  role        = aws_iam_role.s3_rds.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
      {
          "Effect": "Allow",
          "Action": "s3:ListAllMyBuckets",
          "Resource": "*"
      },
      {
          "Effect": "Allow",
          "Action": [
              "s3:ListBucket",
              "s3:GetBucketACL",
              "s3:GetBucketLocation"
          ],
          "Resource": "arn:aws:s3:::${aws_s3_bucket.s3.bucket}"
      },
      {
          "Effect": "Allow",
          "Action": [
              "s3:GetObject",
              "s3:PutObject",
              "s3:DeleteObject*",
              "s3:ListMultipartUploadParts",
              "s3:AbortMultipartUpload"
          ],
          "Resource": "arn:aws:s3:::${aws_s3_bucket.s3.bucket}/*"
      }
    ]
}
EOF
}