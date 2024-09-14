from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as lambda_function
)
from constructs import Construct

class CdkGitHubStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #example resource
        queue = sqs.Queue(
             self, "CdkGitHubQueue",
             visibility_timeout=Duration.seconds(300),
        )

        bucket = s3.Bucket(self, "MyfirstBucket", versioned=True,
                           bucket_name="demo-bucket-learning123",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)