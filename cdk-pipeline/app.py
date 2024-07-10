#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.cdk_pipeline_stack import CdkPipelineStack


app = cdk.App()
CdkPipelineStack(
    app, "CdkCodePipelineStack",
    env=cdk.Environment(
        account='123456789012', # Pipeline management AWS account
        region='us-east-1'
    )
)

app.synth()
