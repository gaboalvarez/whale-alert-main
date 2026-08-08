import datetime
import boto3
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from botocore.exceptions import NoCredentialsError, EndpointConnectionError


def check_s3_connection():
    try:
        s3_client = boto3.client(
            's3',
            endpoint_url='http://data-lake:9000',
            aws_access_key_id='minio',
            aws_secret_access_key='minio123',
            region_name='us-east-1',
            config=boto3.session.Config(signature_version='s3v4')
        )

        response = s3_client.list_buckets()
        print("Connection to MinIO is successful!")
        print("Buckets: ", [bucket['Name'] for bucket in response['Buckets']])

    except NoCredentialsError:
        print("Error: No valid credentials provided!")
    except EndpointConnectionError:
        print("Error: Unable to connect to the endpoint!")
    except Exception as e:
        print(f"An error occurred: {e}")

with DAG(
    dag_id="test_minio_connection",
    start_date=datetime.datetime(2025, 1, 31),
    schedule=None,
    catchup=False,
    tags=["infrastructure"],
):
    PythonOperator(task_id="check_connection", python_callable=check_s3_connection)