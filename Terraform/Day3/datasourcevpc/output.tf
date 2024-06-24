# Output the details of the existing instance
root@ip-172-31-43-107:/home/ubuntu/test1# cat output.tf 
output "instance_details" {
  value = {
    id               = data.aws_instance.existing_instance.id
    instance_type    = data.aws_instance.existing_instance.instance_type
    private_ip       = data.aws_instance.existing_instance.private_ip
    public_ip        = data.aws_instance.existing_instance.public_ip
    availability_zone = data.aws_instance.existing_instance.availability_zone
    # Add more attributes as needed
  }
}
