from diagrams import Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet

# Output filename for this diagram
OUTPUT_FILENAME = "aws_three_tier"


def create_diagram() -> None:
    """Define a classic AWS three-tier architecture."""
    user = Internet("Users")

    with Cluster("CDN"):
        cdn = CloudFront("CloudFront")

    with Cluster("Load Balancer"):
        lb = ELB("Application Load Balancer")

    with Cluster("Web Tier"):
        web_servers = [EC2("Web Server 1"), EC2("Web Server 2"), EC2("Web Server 3")]

    with Cluster("Application Tier"):
        app_servers = [EC2("App Server 1"), EC2("App Server 2")]

    with Cluster("Database Tier"):
        primary_db = RDS("Primary DB")
        replica_db = RDS("Read Replica")

    with Cluster("Storage"):
        storage = S3("S3 Bucket")

    # Define connections
    user >> cdn >> lb >> web_servers
    web_servers >> app_servers
    app_servers >> primary_db
    app_servers >> replica_db
    app_servers >> storage
