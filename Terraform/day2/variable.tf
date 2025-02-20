output "instance_public_ip" {
  description = "The public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

variable ami {
        description = "ami of the iserver"
}

variable instance_type {
        description = "instance type of server"
}

variable aws_region1 {
        description = "Region where we need to create"
        default = "us-east-1"
}
