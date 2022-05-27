import os
from dotenv import load_dotenv

import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

# Get neccessary settings from the dotenv file
load_dotenv()

BACKEND_IMG = os.getenv("BACKEND_IMG")
backend_port = os.getenv("BACKEND_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT","")

# availability_zone = “ap-northeast-2”

cluster = aws.ecs.Cluster("mlopscurriculum")

db_lb = awsx.lb.ApplicationLoadBalancer("postgres-lb")
postgres = awsx.ecs.FargateService("postgres",
    cluster=cluster.arn,
    desired_count=2,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image="postgres",
            name="postgres",
            cpu=512,
            memory=128,
            essential=True,
            port_mappings=[awsx.ecs.TaskDefinitionPortMappingArgs(
                target_group=db_lb.default_target_group,
            )],
            environment=[
                {"name": "POSTGRES_DB", "value": db_name},
                {"name": "POSTGRES_USER", "value": db_user},
                {"name": "POSTGRES_PASSWORD", "value": db_password},
                {"name": "POSTGRES_HOST", "value": db_host},
                {"name": "POSTGRES_PORT", "value": db_port},
            ],
            
        )
    )
)

back_lb = awsx.lb.ApplicationLoadBalancer("back-lb")
service = awsx.ecs.FargateService("backend",
    cluster=cluster.arn,
    desired_count=2,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image=BACKEND_IMG,
            cpu=512,
            memory=128,
            essential=True,
            port_mappings=[awsx.ecs.TaskDefinitionPortMappingArgs(
                target_group=back_lb.default_target_group,
            )],
            environment=[
                # {"name": "BACKEND_PORT", "value": backend_port},
            ]
        )
    )
)