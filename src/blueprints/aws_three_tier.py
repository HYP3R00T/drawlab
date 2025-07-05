from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet


def create_aws_three_tier_diagram(
    filename: str = "output/aws_three_tier",
    title: str = "AWS Three-Tier Architecture",
    direction: str = "TB",
    show: bool = False,
) -> None:
    with Diagram(title, filename=filename, direction=direction, show=show):
        user = Internet("Users")

        with Cluster("CDN"):
            cdn = CloudFront("CloudFront")

        with Cluster("Load Balancer"):
            lb = ELB("Application Load Balancer")

        with Cluster("Web Tier"):
            web_servers = [
                EC2("Web Server 1"),
                EC2("Web Server 2"),
                EC2("Web Server 3"),
            ]

        with Cluster("Application Tier"):
            app_servers = [EC2("App Server 1"), EC2("App Server 2")]

        with Cluster("Database Tier"):
            primary_db = RDS("Primary DB")
            replica_db = RDS("Read Replica")

        with Cluster("Storage"):
            storage = S3("S3 Bucket")

        # Define connections
        user >> cdn >> lb
        lb >> web_servers[0]
        lb >> web_servers[1]
        lb >> web_servers[2]

        for web in web_servers:
            for app in app_servers:
                web >> app

        for app in app_servers:
            app >> primary_db
            app >> replica_db
            app >> storage
