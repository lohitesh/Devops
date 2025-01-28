import boto3
import os

ec2 = boto3.client("ec2")
key_pair_name = "pyuser"

response = ec2.create_key_pair(KeyName=key_pair_name)
local_key = f"{key_pair_name}.pem

with open(local_key, "w") as f:
  f.write(response['KeyMaterial'])
f.close()

print(f"Key {key_pair_name} created on AWS.")
print(f"Key {local_key} created on local VM.")

os.chmod(local_key,0o400)
print(f"Key {local_key} permission changed to 400")


# Line 3 creates a client for the EC2 service, which allows user to interact with EC2 instances, security groups, key pairs, and other EC2 resources through Python.
# after creating key pair it will return three key value pair 'KeyName': 'pyuser', 'KeyFingerprint': 'string', 'KeyMaterial': "keys"
# os.chmod(local_key,0o400)    ------ octal format representation
