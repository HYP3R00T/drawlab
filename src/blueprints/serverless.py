from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.onprem.network import Internet


def create_serverless_diagram(
    filename: str = "output/serverless_architecture",
    title: str = "Serverless Architecture",
    direction: str = "TB",
    show: bool = False,
) -> None:
    with Diagram(title, filename=filename, direction=direction, show=show):
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
        api >> auth_lambda
        api >> user_lambda
        api >> order_lambda
        user_lambda >> user_db
        order_lambda >> order_db
        user_lambda >> file_storage
        order_lambda >> file_storage
