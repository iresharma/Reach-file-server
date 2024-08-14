import os
import boto3
from json import dumps
from r2 import utils
from r2.utils import convert_response, convert_size
from botocore.exceptions import NoCredentialsError, ClientError


class R2Wrapper:
    def __init__(self):
        self.endpoint = os.environ.get("ENDPOINT")
        self.access_key_id = os.environ.get("KEY_ID")
        self.secret_key = os.environ.get("SECRET_KEY")
        self.region_name = 'apac'
        self.client = boto3.client(
            's3',
            endpoint_url=self.endpoint,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_key,
            region_name=self.region_name,
        )

    def init_bucket(self, bucket_name, account_info):
        self.client.create_bucket(Bucket=bucket_name)
        account_info["updated_at"] = str(account_info["updated_at"])
        account_info["created_at"] = str(account_info["created_at"])
        data = dumps(account_info, indent=4)
        self.client.put_object(Body=data, Bucket=bucket_name, Key='accountInfo.txt')

    def list_bucket(self, bucket_name, path: str = "/"):
        path = 'userData' + path

        result = self.client.list_objects_v2(Bucket=bucket_name, Prefix=path, Delimiter='/')
        response = {'files': list(map(lambda x: utils.process_file(x, path), result.get('Contents'))),
                    'folders': list(map(lambda x: x['Prefix'].replace(path, ''), result.get('CommonPrefixes')))}

        response['files'] = list(map(convert_response, response.get('files')))
        return response

    def create_folder(self, bucket_name: str, path: str):
        path = 'userData' + path
        result = self.client.put_object(Bucket=bucket_name, Key=path + '/')

    def pre_signed_get(self, bucket_name: str, object_key: str, expiration: int = 3600):
        try:
            response = self.client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': object_key
                },
                ExpiresIn=expiration
            )
        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print("The object does not exist.")
                return None
            else:
                print(f"Unexpected error: {e}")
                return None
        return response

    def pre_signed_delete(self, bucket_name: str, object_key: str, expiration: int = 3600):
        try:
            response = self.client.generate_presigned_url(
                'delete_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': object_key
                },
                ExpiresIn=expiration
            )
        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print("The object does not exist.")
                return None
            else:
                print(f"Unexpected error: {e}")
                return None
        return response

    def delete_object(self, bucket_name: str, object_key: str):
        try:
            response = self.client.delete_object(Bucket=bucket_name, Key=object_key)
        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print("The object does not exist.")
                return None
            else:
                print(f"Unexpected error: {e}")
                return None
        return response

    def pre_signed_put(self, bucket_name: str, object_key: str, expiration: int = 3600):
        try:
            response = self.client.generate_presigned_url(
                'put_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': object_key
                },
                ExpiresIn=expiration
            )
        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print("The object does not exist.")
                return None
            else:
                print(f"Unexpected error: {e}")
                return None
        return response

    def get_bucket_metadata(self, bucket_name: str):
        s3_client = self.client
        metadata = {
            'TotalSize': 0,
            'ObjectCount': 0
        }

        try:
            # Get bucket creation date (requires list_buckets permission)
            buckets = s3_client.list_buckets()
            for bucket in buckets['Buckets']:
                if bucket['Name'] == bucket_name:
                    metadata['CreationDate'] = bucket['CreationDate'].strftime("%Y-%m-%d %H:%M:%S")

            # List objects and calculate total size and count
            paginator = s3_client.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=bucket_name)

            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        metadata['TotalSize'] += obj['Size']
                        metadata['ObjectCount'] += 1
            metadata['TotalSize'] = convert_size(metadata['TotalSize'])
            return metadata

        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            print(f"Error retrieving bucket metadata: {e}")
            return None