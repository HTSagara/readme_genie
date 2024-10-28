<!-- omit in toc -->

# Contributing to ReadmeGenie

First off, thanks for taking the time to contribute!## Getting Started

This guide will help you get started with **Readme Genie** using either Docker or a local Python environment.

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/) if you plan to use Docker.
- **Python 3.12**: [Install Python](https://www.python.org/downloads/) if you plan to run the script locally without Docker.
- **API Keys**: You will need an API key for Groq or Cohere.

## Running with Docker

### Step 1: Build the Docker Image

Before running the script, you need to build the Docker image. Run the following command in the project's root directory (where the `Dockerfile` is located):

```bash
docker build -t readmegenie:latest .
```

### Step 2: Install Required Packages

Ensure that all required Python packages are installed inside the Docker container by executing:

```bash
docker run --rm -v "$(pwd)":/app readmegenie:latest pip install -r requirements.txt
```

### Step 3: Run the Script

To generate a README file, use the following command:

```bash
docker run --rm -v "$(pwd)":/app readmegenie:latest python3 readme_genie.py [OPTIONS] <file1> <file2> ...
```

Alternatively, use the provided `generate-readme.sh` script:

```bash
./generate-readme.sh [OPTIONS] <file1> <file2> ...
```

### Example Commands

Here is an example command to generate a `README.md` file using Docker:

```bash
docker run --rm -v "$(pwd)":/app readmegenie:latest python3 readme_genie.py path/to/file1.py path/to/file2.py -a your_api_key -u https://api.groq.com -o README.md -t
```

### Arguments

- **`file_paths`**: A list of file paths from which the content will be used to generate the README.
- **`-a`, `--api-key`**: Your Groq or Cohere API key.
- **`-u`, `--base-url`**: The base URL for the Groq or Cohere API.
- **`-o`, `--output`**: The name of the output file (default is `README.md`).
- **`-t`, `--token-usage`**: Flag to include token usage information in the output.

## Running Locally Without Docker

If you prefer to run the script directly on your local machine, follow these steps:

### Step 1: Create a Virtual Environment

First, create a Python virtual environment to isolate your project's dependencies:

```bash
python3 -m venv venv
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment using the command specific to your operating system:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Required Packages

With the virtual environment activated, install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run the Script

Now, you can run the script with the required arguments:

```bash
python readme_genie.py path/to/file1.py path/to/file2.py -a your_api_key -u https://api.groq.com -o README.md -t
```

### Step 4-B: Running the Script with `.toml config file`

1. First, you need to make a `readme_genie-config.toml` file in your local home directory.
   For example:

```bash
api_key="YOUR_API_KEY"
token_usage=true
output="result.md"
base_url="https://api.groq.com"
```

2. Since, docker image is an isolated environment, it cannot access files on your local machine.
   Mount the config file onto your docker image.
   Run the following command.

```bash
docker run --rm -v ~/.readme_genie-config.toml:/root/.readme_genie-config.toml readmegenie:latest python3 /app/readme_genie.py ./examples/javascript/server.js
```

### Deactivating the Virtual Environment

After running the script, you can deactivate the virtual environment by using:

```bash
deactivate
```

## Environment Variables

To use the API keys and base URLs without specifying them in every command, set the following environment variables:

- `GROQ_API_KEY`: Your Groq API key.
- `COHERE_API_KEY`: Your Cohere API key.
- `GROQ_BASE_URL`: The base URL for the Groq API.
- `COHERE_BASE_URL`: The base URL for the Cohere API.
