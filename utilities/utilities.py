import sys
import random
import string
import boto3
sys.path.append('.')
from base_modules.base import BaseObject, command_sleep
from pathlib import Path
from typing import Dict, List

class Utilities(BaseObject):
    def __init__(self):
        super().__init__()

    def bucket_list(self):
        ''' Returns bucket list if logged in from aws cli '''
        return [bucket for bucket in self.s3.buckets.all()]
            

    def object_count_in_bucket(self, bucket_path: str) -> int:
        ''' Returns object count in a bucket'''
        bucket = self.s3.Bucket(bucket_path)
        object_count = 0
        for i in bucket.objects.all():
            object_count = object_count + 1
        return object_count
        
    def get_folders_and_path_in_bucket(self, bucket_path: str) -> Dict[str]:
        folders = {}
        bucket = self.s3.Bucket(bucket_path)
        for object in bucket.objects.all():
            path = Path(object.key).parent
            folders[path] = folders.get(path, 0) + 1
        return folders

    def get_bucket_objects_list(self, bucket_path: str) -> List[Dict, str, List]:
        '''Returns objects in a bucket'''
        response = self.s3client.list_objects(Bucket=bucket_path)['Contents']
        return response

    def upload_to_s3(self, s3_root_path: str, path: str, file_name: str) -> bool and int:
        '''
        Put file to s3. Checks response from aws result.
        s3_root_path : bucket_name
        path : folder_name.file_name
        file_name : file_name
        '''
        try:
            with command_sleep(after=10):
                s3_upload_result = self.s3client.put_object(Bucket=s3_root_path, Key=path, Body=open(f'{file_name}', 'rb'))
            if s3_upload_result['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True, 200
            else:
                return False, 400
        except Exception as ex:
            print("Failed to upload: %s", str(ex))
            return False, 402

    def download_from_s3(self, s3_root_path: str, file_path: str, file_name: str) -> bool:
        '''
        Downloads file from s3 with given s3_root_path, file_path and file_name.
        '''
        try:
            with command_sleep(after=10):
                self.s3client.download_file(Bucket=s3_root_path, Key=file_path, Filename=file_name)
        except Exception as ex:
            print("Failed to download: %s", str(ex))
            return False
        return True

    def random_string(string_length: int = 10) -> str:
        """
        Generate a random string of fixed length to use as a unique id.
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))


ut = Utilities()
ut.respo()