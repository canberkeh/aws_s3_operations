import boto3
import time
import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Any, Optional, Union

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

class CommandSleep:
    """
    Context manager to sleep before and after context execution.
    Usage:
        with command_sleep(before=1, after=2):
            ...
    """

    def __init__(self,
                 before: Optional[Union[float, int]] = None,
                 after: Optional[Union[float, int]] = None,
                 *arg, **kwargs):
        assert before or after
        if before:
            assert before > 0
        if after:
            assert after > 0
        self.before = before
        self.after = after

    def __enter__(self):
        if self.before:
            os.time.sleep(self.before)

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):
        if not exc_value and self.after:
            time.sleep(self.after)

command_sleep = CommandSleep