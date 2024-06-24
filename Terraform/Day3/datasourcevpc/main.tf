provider "aws" {
  region     = var.aws_region
  access_key = "AKIA6ODU36CI7A4J4L7S"
  secret_key = "G5mDUEEWAvWaHoKrE4aBs6islaNhh4wMxdRqjyOP"
}

data "aws_instance" "existing_instance" {
  instance_id = "i-00660cea0163b9853"  # Replace "your-instance-id" with the actual instance ID
}
