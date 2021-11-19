import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

aws_config = { 
    "region_name": os.getenv("region_name"),
    "aws_access_key_id": os.getenv("aws_access_key_id"),
    "aws_secret_access_key": os.getenv("aws_secret_access_key")
}

class BaseObject():
    def __init__(self):
        self.s3client = boto3.client('s3', 
                                    region_name=aws_config["region_name"],
                                    aws_access_key_id=aws_config["aws_access_key_id"],
                                    aws_secret_access_key=aws_config["aws_secret_access_key"])
        self.s3 = boto3.resource("s3")