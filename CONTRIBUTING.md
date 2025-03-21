<!-- omit in toc -->

# Contributing to ReadmeGenie

Thank you for taking the time to contribute to **ReadmeGenie**! Your help is greatly appreciated. This guide will assist you in setting up the project for development, using Docker or a local Python environment, and ensuring that code formatting and linting are consistent.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Running Locally](#running-locally-without-docker)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Required Packages](#install-required-packages)
- [Code Formatting and Linting](#code-formatting-and-linting)
  - [Using Ruff for Linting](#using-ruff-for-linting)
  - [Using Black for Code Formatting](#using-black-for-code-formatting)
  - [Running Formatting and Linting in VS Code](#running-formatting-and-linting-in-vs-code)
- [Running Tests and Checking Coverage](#running-tests-and-checking-coverage)
  - [Testing Commands](#testing-commands)
- [Environment Variables](#environment-variables)

## Getting Started

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/) if you plan to use Docker.
- **Python 3.12**: [Install Python](https://www.python.org/downloads/) if you plan to run the script locally without Docker.
- **API Keys**: You will need an API key for Groq or Cohere.

## Running Locally Without Docker

Clone the project into you local machine

### Set Up a Virtual Environment

Create a Python virtual environment to isolate your project’s dependencies:

```bash
python3 -m venv venv
```

### Install Required Packages

With the virtual environment activated, install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Run the Script

Run the script with the required arguments:

```bash
python src/readme_genie.py <path/to/file1.py> <path/to/file2.py> -a <your_api_key> -u <https://api.groq.com> -o <file_name>.md -t
```

Example running with GROQ:

```bash
python src/readme_genie.py src/examples/javascript/routes.js -a <GROQ_API_KEY> -u https://api.groq.com
```

Example running with Cohere:

```bash
python src/readme_genie.py src/examples/javascript/routes.js -a <COHERE_API_KEY> -u https://api.cohere.ai/v1
```

## Code Formatting and Linting

We use **Ruff** for linting and **Black** for code formatting. These tools help ensure code consistency and readability across the project. They are configured in `pyproject.toml` for easy setup.

### Pre-Commit Hooks for Automatic Linting and Formatting

For a consistent development experience, pre-commit hooks are used to automatically check code quality before each commit. Install pre-commit hooks by running:

```bash
pre-commit install
```

This will enforce Ruff and Black checks on your code upon every `git commit`. To run these checks manually, use:

```bash
pre-commit run --all-files
```

### Using Ruff for Linting

Ruff is configured to handle linting tasks without making any code changes. To run Ruff as the linter:

```bash
ruff check . --fix
```

Ruff configurations are set to avoid conflicts with Black, and you can see detailed settings in `pyproject.toml`.

### Using Black for Code Formatting

To format the code with Black, run:

```bash
black .
```

This will apply the Black formatting conventions to all Python files in the project.

### Running Formatting and Linting in VS Code

If you’re using VS Code, you can set up the following configuration in `.vscode/settings.json` to run Ruff and Black automatically on file save:

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll.ruff": true
  }
}
```

This setup ensures that Black formats the code, while Ruff handles linting, every time you save a file.

## Running Tests and Checking Coverage

Unit tests ensure that **ReadmeGenie** functions correctly and meets quality standards. We use `unittest` for testing and `coverage` to monitor code coverage.

### Testing Commands

To run all tests and check coverage, use the following commands:

```bash
# Run all tests and collect coverage data
coverage run --source=. -m unittest discover -s tests

# Generate a detailed coverage report
coverage report -m
```

This will show you which lines of code were tested, making it easier to identify untested areas.

A pre-commit hook is configured to enforce a minimum test coverage percentage of 75% on each commit. This ensures that all code changes meet the required coverage threshold before they are committed.

## Environment Variables

To use the API keys and base URLs without specifying them in every command, set the following environment variables:

- `GROQ_API_KEY`: Your Groq API key.
- `COHERE_API_KEY`: Your Cohere API key.
- `GROQ_BASE_URL`: The base URL for the Groq API.
- `COHERE_BASE_URL`: The base URL for the Cohere API.

Thank you for contributing to **Readme Genie**! Your work and efforts are appreciated.
