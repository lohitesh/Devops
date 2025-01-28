import boto3

s3 = boto3.client("s3")
bucketname = input("Enter the bucket to list files of: ")
items = s3.list_objects_v2(Bucket=bucketname)

print(f"Bucket Name: {bucketname}")
print(f"Bucket Content: ")

for item in items['Contents']:
	print(f"\t ---> {item['key']}")
