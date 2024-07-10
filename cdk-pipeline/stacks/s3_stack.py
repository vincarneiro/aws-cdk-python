from constructs import Construct
import json
from aws_cdk import (
    aws_s3 as s3,
    Stack
)

class S3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, env_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Read enfironments file
        with open("config.json") as f:
            config = json.load(f)

        s3.Bucket(
          self,
          id=f"{config['service']}-{env_name}",
          object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
          block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )