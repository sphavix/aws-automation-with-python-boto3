import boto3
import os
from botocore.exceptions import ClientError

def get_aws_region():
    """
    Get AWS region with multiple fallback options
    """
    
    region = (
        boto3.session.Session().region_name or
        #os.environ.get('AWS_DEFAULT_REGION') or
        #os.environ.get('AWS_REGION') or
        'eu-north-1'
    )
    return region

def create_bucket_with_fallback(bucket_name, region=None):
    """
    Create bucket with comprehensive region handling
    """
    if region is None:
        region = get_aws_region()
    
    print(f"Target region: {region}")
    
    try:
        s3 = boto3.client('s3', region_name=region)
        
        # Check bucket existence
        try:
            s3.head_bucket(Bucket=bucket_name)
            print(f"✓ Bucket '{bucket_name}' already exists")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] != '404':
                raise e
        
        # Create bucket
        create_params = {'Bucket': bucket_name}
        if region != 'us-east-1':
            create_params['CreateBucketConfiguration'] = {
                'LocationConstraint': region
            }
        
        s3.create_bucket(**create_params)
        print(f"✓ Bucket '{bucket_name}' created successfully in {region}")
        return True
        
    except ClientError as e:
        print(f"✗ Failed to create bucket: {e}")
        return False

# Upload file to the bucket
def upload_file1_to_bucket():
    """
    Upload a file to the bucket
    """
    bucket_name = 's3-crud-bucket-0101'
    file_name = 'file1.txt'
    
    s3 = boto3.client('s3')
    
    try:
        s3.upload_file(file_name, bucket_name, Key=file_name)
        print(f"✓ File '{file_name}' uploaded to bucket '{bucket_name}'")
    except ClientError as e:
        print(f"✗ Failed to upload file: {e}")

# Read content from a file in the S3 bucket
def read_content_from_file1_in_s3():
    """
    Read content from a file in the S3 bucket
    """
    bucket_name = 's3-crud-bucket-0101'
    file_name = 'file1.txt'
    
    s3 = boto3.client('s3')
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = response['Body'].read().decode('utf-8')
        print(f"✓ Content of '{file_name}':\n{content}")
        return content
    except ClientError as e:
        print(f"✗ Failed to read file: {e}")
        return None

# Update the content of file1 in the S3 bucket with file1 content
def update_content_from_file1_in_s3_bucket():
    """
    Update content of a file1.txt in the S3 bucket with contents from file2.txt
    """
    bucket_name = 's3-crud-bucket-0101'
    file1_name = 'file1.txt'
    file2_name = 'file2.txt'
    
    s3 = boto3.client('s3')
    
    try:
        # Read content from file2.txt
        with open(file2_name, 'r') as f:
            content = f.read()
        
        # Upload updated content to S3
        s3.put_object(Bucket=bucket_name, Key=file1_name, Body=content)
        print(f"✓ Updated '{file1_name}' in bucket '{bucket_name}' with contents from '{file2_name}'")
    except ClientError as e:
        print(f"✗ Failed to update file: {e}")

def delete_bucket_and_contents():
    """
    Delete a bucket and all its contents
    """
    bucket_name = 's3-crud-bucket-0101'
    s3 = boto3.client('s3')
    
    try:
        # List objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        
        # Delete all objects
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        print(f"✓ Bucket '{bucket_name}' deleted successfully")
    except ClientError as e:
        print(f"✗ Failed to delete bucket: {e}")

# Usage examples
if __name__ == "__main__":
    # Method 1: Auto-detect region
    create_bucket_with_fallback('s3-crud-bucket-0101')
    
    #upload_file1_to_bucket()
    upload_file1_to_bucket()

    # Read content from the file
    read_content_from_file1_in_s3()

    # Update content in the file
    update_content_from_file1_in_s3_bucket()

    # Delete the bucket and its contents
    delete_bucket_and_contents()
    
    # Method 2: Specify region explicitly
    #create_bucket_with_fallback('s3-crud-bucket-2', 'eu-west-1')
    
    # Method 3: Force us-east-1
    #create_bucket_with_fallback('s3-crud-bucket-3', 'us-east-1')