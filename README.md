# DrawLab - Simple Diagram Generation

A straightforward system for generating infrastructure and architecture diagrams using the Python `diagrams` library. No over-engineering - just simple functions that create diagrams.

## Structure

- **Blueprint files**: Each diagram type has its own file in `src/blueprints/`
- **Simple functions**: Each blueprint has one function that accepts parameters
- **Direct usage**: Import and call functions directly in `main.py`

## Usage

Each blueprint function accepts these parameters:
- `filename`: Output path (default: `"output/diagram_name"`)
- `title`: Diagram title
- `direction`: Layout direction (`"TB"`, `"LR"`, `"BT"`, `"RL"`)
- `show`: Whether to display after generation (default: `False`)

### Example Usage

```python
from src.blueprints.homelab import create_homelab_diagram
from src.blueprints.aws_three_tier import create_aws_three_tier_diagram

# Generate with defaults
create_homelab_diagram()

# Generate with custom parameters
create_aws_three_tier_diagram(
    filename="my_custom_aws_diagram",
    title="My AWS Setup",
    direction="LR",
    show=True
)
```

### Available Diagrams

- `create_homelab_diagram()` - Homelab with Kubernetes apps
- `create_aws_three_tier_diagram()` - Classic AWS three-tier architecture
- `create_serverless_diagram()` - AWS Lambda serverless architecture
- `create_kubernetes_diagram()` - Kubernetes deployment setup
- `create_data_pipeline_diagram()` - Data processing pipeline

## Creating New Diagrams

1. Create a new file in `src/blueprints/your_diagram.py`
2. Write a function that accepts the standard parameters
3. Use the `Diagram` context manager with your parameters
4. Import and call it in `main.py`

```python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2

def create_my_diagram(
    filename: str = "output/my_diagram",
    title: str = "My Diagram",
    direction: str = "TB",
    show: bool = False,
) -> None:
    """Create my custom diagram."""
    with Diagram(title, filename=filename, direction=direction, show=show):
        # Your diagram logic here
        server = EC2("Web Server")
```

## Running

```bash
mise drawlab
# or
python -m src.main
```

## Dependencies

- `diagrams>=0.24.4`: Core diagramming library

That's it - simple and straightforward!
