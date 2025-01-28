#!/usr/bin/env python3.9
import boto3
import argparse
parser = argparse.ArgumentParser(prog='s3 File Upload',
			                          description='Python Utility to upload a file on s3',
			                          epilog='This script is only for Python training purpose')

parser.add_argument("file", help="The local file to upload on bucket")
parser.add_argument("bucket",help="The bucket on which to upload the file")
parser.add_argument("--name","-n"help="THe new name of the file on s3")
args = parser.parse_args()

s3 = boto3.client("s3")

if args.anme:
	s3.upload_file(args.file,args.bucket,args.name)	
	print(f"File Uploaded: {args.file}")
	print(f"Bucket Name: {args.bucket}")
	print(f"New Name: {args.name}")
else:
	s3.upload_file(args.file, args.bucket, args.file)	
	print(f"File Uploaded: {args.file}")
	print(f"Bucket Name: {args.bucket}")
	print(f"New Name: {args.file}")


