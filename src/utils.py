from pathlib import Path
from typing import Callable, Any
import logging

from diagrams import Diagram


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_diagram(
    filename: str | Path,
    diagram_function: Callable[[], None],
    title: str = "Diagram",
    direction: str = "TB",
    show: bool = False,
    **diagram_kwargs: Any,
) -> None:
    """Generate a diagram using the provided diagram function.

    Args:
        filename: Output filename for the diagram (with or without extension).
                 Can be a string or Path object.
        diagram_function: Function that defines the diagram structure.
                         Should contain the diagram logic (nodes, clusters, connections).
        title: Title of the diagram.
        direction: Direction of the diagram layout ("TB", "LR", "BT", "RL").
        show: Whether to display the diagram after generation.
        **diagram_kwargs: Additional keyword arguments to pass to the Diagram constructor.

    Raises:
        ValueError: If filename is empty or invalid.
        TypeError: If diagram_function is not callable.
    """
    if not filename:
        raise ValueError("Filename cannot be empty")

    if not callable(diagram_function):
        raise TypeError("diagram_function must be callable")

    # Convert to Path for validation, then to string for diagrams library compatibility
    path_obj = Path(filename)
    filename_str = str(path_obj)

    logger.info(f"Generating diagram '{title}': {filename_str}")

    # Merge default diagram settings with any additional kwargs
    diagram_settings = {
        "show": show,
        "direction": direction,
        "filename": filename_str,
        **diagram_kwargs,
    }

    with Diagram(title, **diagram_settings):
        diagram_function()

    logger.info(f"Diagram '{title}' generated successfully")


def generate_multiple_diagrams(
    diagrams_config: list[tuple[object, str, str]],
    output_dir: str | Path = "output",
) -> None:
    """Generate multiple diagrams from a configuration list.

    Args:
        diagrams_config: list of tuples containing (module, title, direction).
                        Each module should have 'create_diagram' function and 'OUTPUT_FILENAME' attribute.
        output_dir: Directory where diagrams will be saved.

    Returns:
        None
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    successful_generations = 0
    total_diagrams = len(diagrams_config)

    # Generate each diagram
    for diagram_module, title, direction in diagrams_config:
        try:
            output_filename = output_path / diagram_module.OUTPUT_FILENAME

            generate_diagram(
                filename=output_filename,
                diagram_function=diagram_module.create_diagram,
                title=title,
                direction=direction,
            )

            successful_generations += 1

        except Exception as e:
            logger.error(f"Failed to generate {title}: {e}")
            continue

    logger.info(
        f"Generated {successful_generations}/{total_diagrams} diagrams successfully"
    )
    logger.info(f"Output directory: {output_path.absolute()}")
