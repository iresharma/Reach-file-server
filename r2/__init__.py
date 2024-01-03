import boto3
from os import environ
from json import dumps

s3 = boto3.client('s3',
                  endpoint_url=environ.get('R2_DOMAIN'),
                  aws_access_key_id=environ.get("ACCESS_KEY_ID"),
                  aws_secret_access_key=environ.get('SECRET_KEY')
                  )


def list():
    response = s3.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    print(dumps(response, indent=4))
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


def create(bucket_name):
    response = s3.create_bucket(Bucket=bucket_name)
    print('Created bucket')
    print(dumps(str(response), indent=4))


def put():
    bucket = "temp-reach-bucket"
    s3.put_object(
        Body=open('/Users/iresharma/Documents/FileServer/r2/test.png', 'rb'),
        Bucket=bucket,
        Key="test.png"
    )
