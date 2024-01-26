import boto3
from json import dumps
import utils

class R2Wrapper:
    def __init__(self, endpoint, access_key_id, secret_key, region_name):
        self.endpoint = endpoint
        self.access_key_id = access_key_id
        self.secret_key = secret_key
        self.region_name = region_name
        self.client = boto3.client('s3',
                                   endpoint_url=endpoint,
                                   aws_access_key_id=access_key_id,
                                   aws_secret_access_key=secret_key,
                                   region_name=region_name,
                                   )

    def init_bucket(self, bucket_name, accountInfo):
        self.client.create_bucket(Bucket=bucket_name)
        self.client.put_object(Body=dumps(accountInfo, indent=4), Bucket=bucket_name, Key='accountInfo.txt')

    def list_bucket(self, bucket_name, path):
        path = 'userData' + path

        result = self.client.list_objects_v2(Bucket=bucket_name, Prefix=path, Delimiter='/')
        response = {'files': list(map(lambda x: utils.process_file(x, path), result.get('Contents'))),
                    'folders': list(map(lambda x: x['Prefix'].replace(path, ''), result.get('CommonPrefixes')))}
        for o in response.get('files'):
            print('File : ', o.get('filename'))
        for o in response.get('folders'):
            print('sub folder : ', o)

        print(dumps(response, indent=4))

    def create_folder(self, bucket_name: str, path: str):
        path = 'userData' + path
        result = self.client.put_object(Bucket=bucket_name, Key=path+'/')