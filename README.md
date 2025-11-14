# Python LeetCode Solutions

This repository contains Python solutions for LeetCode problems, managed with [uv](https://github.com/astral-sh/uv) - an extremely fast Python package and project manager.

## Project Structure

```
├── gen.py                 # Script to generate new LeetCode problem files
├── leetcode_skeleton.txt  # Template for new LeetCode problem files
├── playground.py          # Scratch file for experimentation
├── problems/              # Directory containing LeetCode problem solutions
├── pyproject.toml         # Project configuration and dependencies
└── uv.lock               # Lock file for reproducible environments
```

## Getting Started

### Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package and project manager
- Python 3.8 or higher

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python_uv_leetcode
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

This will create a virtual environment and install all dependencies specified in `pyproject.toml`.

## Usage

### Running Tests

To run all tests for the LeetCode solutions:
```bash
uv run pytest
```

To run tests for a specific problem:
```bash
uv run pytest problems/0001_two-sum.py
```

### Generating New Problem Files

Use the `gen.py` script to automatically create a new LeetCode problem file based on the template:

```bash
uv run gen.py <problem_number> "<dash-separated-title>"
```

**Examples:**
```bash
# Generate a file for problem 1 - Two Sum
uv run gen.py 1 "two-sum"

# Generate a file for problem 2536 - Increment Submatrices By One
uv run gen.py 2536 "increment-submatrices-by-one"
```

Alternatively, you can run the script without arguments and it will prompt you for input:
```bash
uv run gen.py
```

The generated file will be placed in the `problems/` directory with the naming convention: `<4-digit-number>_<dash-separated-title>.py`

### Working with the Playground

Use `playground.py` for experimentation and testing concepts before implementing them in actual problem solutions.

## Features

- **Fast dependency management** with uv
- **Automated problem file generation** with consistent structure
- **Integrated testing** with pytest
- **Type hints** for better code quality
- **Pre-configured project structure** for LeetCode problem solving

## Dependencies

This project includes the following dependencies (see `pyproject.toml` for complete list):
- `pytest` - For testing solutions
- Development dependencies for code quality and formatting

## Contributing

1. Generate a new problem file using `uv run gen.py`
2. Implement your solution
3. Add test cases in the pytest section
4. Verify your solution works by running `uv run pytest`
5. Commit your changes

## License

This project is intended for personal use and LeetCode problem solving practice.