import boto3

s3=boto3.resource("s3")

bucket=s3.Bucket("test24jun")

bucket.download_file(Key="sample.json",Filename="neerajasample1.json")
