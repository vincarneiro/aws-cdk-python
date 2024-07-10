from constructs import Construct
import json
from aws_cdk import (
    Stage,
    Environment
)
from custom_constructs.vpc import CustomVpcConstruct
from stacks.s3_stack import S3Stack

class DeployStage(Stage):
    def __init__(self, scope: Construct, id: str, env: Environment, stage: str, **kwargs):
        super().__init__(scope, id, **kwargs,)
        
        self.env = env

        # Read enfironments file
        with open("config.json") as f:
            config = json.load(f)

        # Deploy Custom VPC
        CustomVpcConstruct(self, "vpc", vpc_cidr="10.0.0.0/16")

        # Deploy S3 bucket
        S3Stack(
            self,
            "s3_stack",
            stack_name=f"{config['service']}-s3-{env.region}-{env.account}",
            env_name=stage
        )
