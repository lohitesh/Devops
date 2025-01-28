import boto3
s3 = boto3.client("s3")

bucket_name = input("Enter the bucket name")
bucket_location = input("Enter bucket location")

s3.create_bucket(Bucket=bucket_namme, CreateBucketConfiguration={'LocationConstraint':buckket_location})

print(f"Bucket {bucket_name} created")
print(f"Bucket Loation {bucket_location}")

