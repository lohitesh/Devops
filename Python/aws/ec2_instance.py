import boto3
import argparse

parse = argparse.ArgumentParser(description="CLI to create EC2 instance")

parse.add_argument("ami", help="Instance Image ID (ami id) that we need to use for creating e 2 instance")
parse.add_argument("type", help="Instance Type")
parse.add_argument("key", help="ssh key to connect to instance")
parse.add_argument("min", type=int, help="minimum number of instance to create")
parse.add_argument("max", type=int, help="maximum number of instance to create")
args = parse.parse_args()
ec2 = boto3.resource("ec2")


ec2.create_instances(ImageId=args.ami, InstanceType=args.type, KeyName=args.key, MinCount=args.min, MaxCount=args.max)
print("EC2 instance created")
print(f"Instance type: {args.type}"

print(f"Key Used: {args.key}")
print(f"Number of Instances: {args.max}")
print(f"===============================================================================")

ask_user = input("Do you want to list the details of all the instancess")
if ask_user == "yes":
  n=0
  for instance in ec2.instances.all():
    n = n+1
    print(f"Instance ID: {instance.id}")
  	print(f"Instance public IP: {instance.public_ip_address}")
  	print(f"Instance State: {instance.state['Name']})"
  print(f"Total Count: {n}")
else:
  print("Script exited successfully")

# Execute Statement:   python3 ec2_instance.py "ami-rhjkskjfdhkjsh" "t2.micro" pyuser1 1 1
# here pyuser1 file need to exist in aws as well in local machine
  

