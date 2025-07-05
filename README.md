# DrawLab - Diagram Generation System

This project provides a modular and type-safe system for generating infrastructure and architecture diagrams using the Python `diagrams` library. Each diagram is defined in a separate file within the `drawlab.diagrams` package.

## Features

- **Modular design**: Each diagram is in its own file with clear separation of concerns
- **Type-safe**: Full type hints for better code quality and IDE support
- **Flexible diagram generation**: Generic `generate_diagram()` function
- **Self-documenting**: Each diagram file includes its output filename and description
- **Error handling**: Comprehensive error handling and logging
- **Path handling**: Robust path handling using `pathlib.Path`

## Core Function

### `generate_diagram()`

The main function for generating diagrams:

```python
def generate_diagram(
    filename: Union[str, Path],
    diagram_function: Callable[[], None],
    title: str = "Diagram",
    direction: str = "TB",
    show: bool = False,
    **diagram_kwargs: Any
) -> None:
```

**Parameters:**
- `filename`: Output filename (string or Path object)
- `diagram_function`: Function that defines the diagram structure
- `title`: Diagram title (default: "Diagram")
- `direction`: Layout direction - "TB" (top-bottom), "LR" (left-right), "BT" (bottom-top), "RL" (right-left)
- `show`: Whether to display the diagram after generation
- `**diagram_kwargs`: Additional arguments passed to the Diagram constructor


## Creating a New Diagram

### Step 1: Create a new diagram file

Create a new file in `drawlab/diagrams/` (e.g., `my_diagram.py`):

```python
from diagrams import Cluster
from diagrams.programming.language import Python
from diagrams.onprem.database import PostgreSQL

# Output filename for this diagram
OUTPUT_FILENAME = "my_custom_diagram"


def create_diagram() -> None:
    """Define your diagram structure here."""
    app = Python("My Application")
    database = PostgreSQL("Database")

    app >> database
```

### Step 2: Add it to main.py

Update the `diagrams_to_generate` list in `main.py`:

```python
# Import your new diagram
from drawlab.diagrams import my_diagram

# Add to the list
diagrams_to_generate: List[Tuple[object, str, str]] = [
    # ... existing diagrams ...
    (my_diagram, "My Custom Application", "TB"),
]
```

## Running the Application

Generate all diagrams:
```bash
mise drawlab
```

## Dependencies

- `diagrams>=0.24.4`: The core diagramming library
- `pathlib`: Built-in Python library for path handling
- `typing`: Built-in Python library for type hints
- `logging`: Built-in Python library for logging

## Error Handling

The system includes comprehensive error handling:
- Validates input parameters
- Checks if diagram functions are callable
- Provides informative error messages
- Logs generation progress and errors
- Continues processing other diagrams if one fails

## Type Safety

All functions include proper type hints:
- Input validation with type checking
- Clear parameter and return type annotations
- Support for both string and Path objects for filenames

This modular design makes it easy to add new diagrams, maintain existing ones, and provides clear separation between diagram definitions and generation logic.
