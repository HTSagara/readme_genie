# Use the official Python 3.12 image from Docker Hub
FROM python:3.12.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    SETUPTOOLS_SCM_PRETEND_VERSION=0.1.0

# Set the working directory in the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git && \
    rm -rf /var/lib/apt/lists/*

# Copy project configuration files first
COPY pyproject.toml setup.py ./

# Copy the requirements files
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install groq


# Add build argument for cache busting
ARG CACHEBUST=1

# Copy the source code and other necessary files
COPY src/ ./src/
COPY tests/ ./tests/
COPY README.md LICENSE ./

# Initialize git repository (needed for setuptools-scm)
RUN git init && \
    git add . && \
    git config --global user.email "docker@build.local" && \
    git config --global user.name "Docker Build" && \
    git commit -m "Initial commit"

# Install the package in development mode
RUN pip install -e .

# Make sure the script is executable
RUN chmod +x ./src/readme_genie.py

# Set the entrypoint to the main script
ENTRYPOINT ["python3", "/app/src/readme_genie.py"]