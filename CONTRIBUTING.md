<!-- omit in toc -->

# Contributing to ReadmeGenie

Thank you for taking the time to contribute to **ReadmeGenie**! Your help is greatly appreciated. This guide will assist you in setting up the project for development, using Docker or a local Python environment, and ensuring that code formatting and linting are consistent.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Running with Docker](#running-with-docker)
  - [Build the Docker Image](#build-the-docker-image)
  - [Install Required Packages](#install-required-packages)
  - [Run the Script](#run-the-script)
- [Running Locally Without Docker](#running-locally-without-docker)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Required Packages](#install-required-packages)
  - [Run the Script](#run-the-script)
- [Code Formatting and Linting](#code-formatting-and-linting)
  - [Using Ruff for Linting](#using-ruff-for-linting)
  - [Using Black for Code Formatting](#using-black-for-code-formatting)
  - [Running Formatting and Linting in VS Code](#running-formatting-and-linting-in-vs-code)
- [Environment Variables](#environment-variables)

## Getting Started

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/) if you plan to use Docker.
- **Python 3.12**: [Install Python](https://www.python.org/downloads/) if you plan to run the script locally without Docker.
- **API Keys**: You will need an API key for Groq or Cohere.

## Running with Docker

### Build the Docker Image

In the project’s root directory, where the `Dockerfile` is located, build the Docker image:

```bash
docker build -t readmegenie:latest .
```

### Install Required Packages

Ensure that all required Python packages are installed inside the Docker container by executing:

```bash
docker run --rm -v "$(pwd)":/app readmegenie:latest pip install -r requirements.txt
```

### Run the Script

To generate a README file, use the following command:

```bash
docker run --rm -v "$(pwd)":/app readmegenie:latest python3 readme_genie.py [OPTIONS] <file1> <file2> ...
```

You can also use the provided `generate-readme.sh` script:

```bash
./generate-readme.sh [OPTIONS] <file1> <file2> ...
```

## Running Locally Without Docker

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
python readme_genie.py path/to/file1.py path/to/file2.py -a your_api_key -u https://api.groq.com -o README.md -t
```

## Code Formatting and Linting

We use **Ruff** for linting and **Black** for code formatting. These tools help ensure code consistency and readability across the project. They are configured in `pyproject.toml` for easy setup.

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

## Environment Variables

To use the API keys and base URLs without specifying them in every command, set the following environment variables:

- `GROQ_API_KEY`: Your Groq API key.
- `COHERE_API_KEY`: Your Cohere API key.
- `GROQ_BASE_URL`: The base URL for the Groq API.
- `COHERE_BASE_URL`: The base URL for the Cohere API.

Thank you for contributing to **Readme Genie**! Your work and efforts are appreciated.
