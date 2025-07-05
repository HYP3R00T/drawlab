from diagrams import Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet

# Output filename for this diagram
OUTPUT_FILENAME = "serverless_architecture"


def create_diagram() -> None:
    """Define a serverless architecture with AWS Lambda."""
    user = Internet("Users")

    with Cluster("API Gateway"):
        api = APIGateway("API Gateway")

    with Cluster("Compute"):
        auth_lambda = Lambda("Auth Function")
        user_lambda = Lambda("User Function")
        order_lambda = Lambda("Order Function")

    with Cluster("Database"):
        user_db = Dynamodb("User Table")
        order_db = Dynamodb("Order Table")

    with Cluster("Storage"):
        file_storage = S3("File Storage")

    # Define connections
    user >> api
    api >> [auth_lambda, user_lambda, order_lambda]
    user_lambda >> user_db
    order_lambda >> order_db
    [user_lambda, order_lambda] >> file_storage
