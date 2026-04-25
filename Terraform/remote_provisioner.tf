provider "aws" {
  region = "ap-south-1"
}

# Security group to allow SSH + HTTP
resource "aws_security_group" "web_sg" {
  name = "web-sg-remote-exec"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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

# EC2 instance
resource "aws_instance" "web" {
  ami           = "ami-0f58b397bc5c1f2e8" # Ubuntu (ap-south-1)
  instance_type = "t2.micro"
  key_name      = "your-keypair-name"

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  associate_public_ip_address = true

  tags = {
    Name = "RemoteExecServer"
  }

  # SSH connection
  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("path/to/your/private-key.pem")
    host        = self.public_ip
  }


#local provisioner 
#👉 Uses && so next command runs only if previous succeeds.
provisioner "local-exec" {
  command = "echo Instance IP is ${self.public_ip} && echo RUNNING"
}



#file provisioner
provisioner "file" {
  source      = "local-file-path"
  destination = "remote-file-path"
}


  # Remote exec provisioner
  provisioner "remote-exec" {
    inline = [
      "echo Connected to server",
      "sudo apt update -y",
      "sudo apt install maven -y"
    ]
  }
}
