from src.blueprints import (
    aws_three_tier,
    data_pipeline,
    homelab,
    kubernetes,
    serverless,
)
from src.utils import generate_multiple_diagrams


def main() -> None:
    diagrams_to_generate: list[tuple[object, str, str]] = [
        (homelab, "Homelab Overview", "TB"),
        (aws_three_tier, "AWS Three-Tier Architecture", "TB"),
        (serverless, "Serverless Architecture", "TB"),
        (kubernetes, "Kubernetes Deployment", "LR"),
        (data_pipeline, "Data Processing Pipeline", "LR"),
    ]

    generate_multiple_diagrams(diagrams_to_generate)


if __name__ == "__main__":
    main()
