from pathlib import Path
from src.blueprints.homelab import create_homelab_diagram
from src.blueprints.aws_three_tier import create_aws_three_tier_diagram
from src.blueprints.data_pipeline import create_data_pipeline_diagram
from src.blueprints.kubernetes import create_kubernetes_diagram
from src.blueprints.serverless import create_serverless_diagram


def main() -> None:
    Path("output").mkdir(exist_ok=True)

    create_homelab_diagram()
    create_aws_three_tier_diagram()
    create_serverless_diagram()
    create_kubernetes_diagram()
    create_data_pipeline_diagram()

    print("All diagrams generated successfully!")


if __name__ == "__main__":
    main()
