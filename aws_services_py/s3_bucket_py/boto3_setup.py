import boto3


# List all buckets
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)