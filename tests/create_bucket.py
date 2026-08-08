# create virtual env in python -> https://docs.python.org/3/library/venv.html
# list_buckets -> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_buckets.html
# create_bcuket -> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html
import boto3

BUCKET_NAME = "my-bucket"

s3 = boto3.client("s3", endpoint_url="http://localhost:9000",  aws_access_key_id="minio",aws_secret_access_key="minio123",region_name="us-east-1")

buckets = []
for b in s3.list_buckets()["Buckets"]:
    buckets.append(b["Name"])

#s3_client.create_bucket(Bucket=BUCKET_NAME)

if BUCKET_NAME not in buckets:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' created.")
else:
    print(f"Bucket '{BUCKET_NAME}' already exists.")