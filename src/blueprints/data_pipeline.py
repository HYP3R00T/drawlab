from diagrams import Cluster
from diagrams.aws.analytics import Kinesis, Glue
from diagrams.aws.database import RDS
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3

# Output filename for this diagram
OUTPUT_FILENAME = "data_pipeline"


def create_diagram() -> None:
    """Define a data processing pipeline."""
    data_source = S3("Raw Data")

    with Cluster("Ingestion"):
        stream = Kinesis("Data Stream")

    with Cluster("Processing"):
        etl = Glue("ETL Jobs")

    with Cluster("Storage"):
        processed_data = S3("Processed Data")
        data_warehouse = RDS("Data Warehouse")

    with Cluster("Analytics"):
        ml_model = Sagemaker("ML Model")

    # Define connections
    data_source >> stream >> etl
    etl >> processed_data
    etl >> data_warehouse
    processed_data >> ml_model
