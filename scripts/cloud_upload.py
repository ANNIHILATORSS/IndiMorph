import os
import boto3
from google.cloud import storage as gcs_storage
from azure.storage.blob import BlobServiceClient

def upload_to_cloud(filepath):
    provider = os.environ.get('CLOUD_PROVIDER', 'aws')
    if provider == 'aws':
        s3 = boto3.client('s3')
        bucket = os.environ['S3_BUCKET']
        s3.upload_file(filepath, bucket, os.path.basename(filepath))
        print(f'Uploaded {filepath} to S3 bucket {bucket}')
    elif provider == 'gcp':
        client = gcs_storage.Client()
        bucket = client.bucket(os.environ['GCS_BUCKET'])
        blob = bucket.blob(os.path.basename(filepath))
        blob.upload_from_filename(filepath)
        print(f'Uploaded {filepath} to GCS bucket {bucket.name}')
    elif provider == 'azure':
        conn_str = os.environ['AZURE_CONN_STR']
        container = os.environ['AZURE_CONTAINER']
        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        blob_client = blob_service_client.get_blob_client(container=container, blob=os.path.basename(filepath))
        with open(filepath, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f'Uploaded {filepath} to Azure container {container}')
    else:
        print('Unknown cloud provider. Skipping upload.') 