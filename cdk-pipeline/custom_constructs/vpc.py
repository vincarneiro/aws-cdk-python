from aws_cdk import CfnOutput
import aws_cdk.aws_ec2 as ec2
from constructs import Construct

class CustomVpcConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc_cidr: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        self.vpc = self._buildVpc(vpc_cidr)

        # Outputs
        CfnOutput(self, "vpc-id",
            value=self.vpc.vpc_id,
            description="VPC ID",
            export_name="VpcId",
        )

    def _buildVpc(self, vpc_cidr: str) -> ec2.Vpc:
        
        # Create VPC
        self.vpc = ec2.Vpc(self, "copilot-vpc",
            max_azs=2,
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public-subnet-copilot",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="private-subnet-copilot",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="isolated-subnet-copilot",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24,
                )
            ],
        )

        return self.vpc