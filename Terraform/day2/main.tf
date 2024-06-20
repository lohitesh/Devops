provider "aws" {
  region = var.aws_region1
  access_key = "AKIAQTUBQ2GU4BVBHEDS"
  secret_key = "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"
}

resource "aws_instance" "web" {
  ami           = var.ami 
  instance_type = var.instance_type

  tags = {
    Name = "HelloWorld"
  }

provisioner "local-exec" {
command="echo Server IP address is ${aws_instance.web.private_ip}"
}

provisioner "remote-exec" {
    inline = [
      "sudo apt update -y",
      "sudo apt install -y nginx",
      "sudo systemctl start nginx",
      "sudo systemctl enable nginx"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"  # Adjust based on your AMI's default user
      private_key = file("path/to/your/private-key.pem")     // private key path
      host        = self.public_ip
    }
  }

}
