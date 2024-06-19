// Before executing go to aws accound and create access key to use in terraform code
// Attach policies to this user based on your requirements. At a minimum, you should attach the "AmazonEC2FullAccess" policy for basic EC2 operations. If you need access to other AWS services, attach the relevant policies accordingly.

provider "aws" {
  region = "us-east-2"
  access_key = "AKIAQ3EGPR6GANHIOVW4"
  secret_key = "7LiYbdTXmM0iQvA292wVjmYZMlA13Y1g3NAjVjYz"
}

resource "aws_instance" "tf-example" {
  ami           = "ami-09040d770ffe2224f"
  count = 2
  instance_type = "t2.micro"
  tags = {
    Name = "tf-example-${count.index}"
  }
}
