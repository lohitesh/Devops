resource "local_file" "pet" {
 filename = "/home/ubuntu/test1/pet.txt"
 content = "we love Devops"
lifecycle {
        create_before_destroy = true
}
}


#better to explain below example

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
lifecycle {
        create_before_destroy = true
}
}

#above example will create resource instance and u can check manually in aws dashboard
#now create new resource by changing name of the resource once the resource was created old resource will be deleted by getting details from terraform state file
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
lifecycle {
        create_before_destroy = true
}
}
