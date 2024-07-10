from constructs import Construct
import json
from aws_cdk import (
    Stack,
    Environment,
    pipelines as pipelines
)
from stages.deploy_stage import DeployStage

class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Read enfironment variables file
        with open("config.json") as f:
            config = json.load(f)

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            pipeline_name=f"{config['service']}-pipeline",
            cross_account_keys=True,
            synth=pipelines.CodeBuildStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection(
                    repo_string=f"{config['gh_repo']['string']}",
                    branch=config['gh_repo']['branch'],
                    connection_arn=config['gh_repo']['codestar_connection_arn']
                ),
                install_commands=["npm i -g aws-cdk"],
                commands=[
                    "npm install -g aws-cdk",
                    "pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        # Create one deploy stage for each environment
        for stage in config['environments']:

            pre_approval_steps = [] if not stage.get('require_approval') else [
                pipelines.ManualApprovalStep(f"Promote to {stage['name']}")
            ]

            pipeline.add_stage(
                stage=DeployStage(
                        self,
                        id=f"Deploy_{stage['name']}",
                        env=Environment(
                            account=stage['account_id'],
                            region=stage['region']
                        ),
                        stage=stage['name']
                    ),
                pre=pre_approval_steps,
            )