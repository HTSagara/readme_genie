#!/bin/bash

# Function to show usage
show_usage() {
    echo "Usage: $0 [options] file1 [file2 ...]"
    echo "Options:"
    echo "  -a API_KEY    Your API key"
    echo "  -u BASE_URL   The base URL (default: https://api.groq.com)"
    echo "  -o OUTPUT     Output filename (default: README.md)"
    exit 1
}

# Initialize variables
BASE_URL="https://api.groq.com"
OUTPUT="README.md"
FILES=()

# Parse command line options
while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--api-key)
            API_KEY="$2"
            shift 2
            ;;
        -u|--base-url)
            BASE_URL="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        -h|--help)
            show_usage
            ;;
        *)
            # If not an option, treat as a file
            FILES+=("$1")
            shift
            ;;
    esac
done

# Check if at least one file is provided
if [ ${#FILES[@]} -eq 0 ]; then
    echo "Error: At least one input file is required"
    show_usage
fi

# Construct the command with all input files
CMD_ARGS=""
for file in "${FILES[@]}"; do
    # Get the directory containing the script
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    
    # Convert to absolute path if relative
    if [[ "$file" = /* ]]; then
        ABS_PATH="$file"
    else
        ABS_PATH="$SCRIPT_DIR/$file"
    fi
    
    # Convert to path relative to /app in container
    REL_PATH="${ABS_PATH#$SCRIPT_DIR/}"
    CMD_ARGS="$CMD_ARGS /app/$REL_PATH"
done

# Build the Docker command
DOCKER_CMD="docker run --rm -v \"$(pwd):/app\" readmegenie:latest"

# Add the files first
DOCKER_CMD="$DOCKER_CMD $CMD_ARGS"

# Add optional arguments
if [ ! -z "$API_KEY" ]; then
    DOCKER_CMD="$DOCKER_CMD -a \"$API_KEY\""
fi

if [ ! -z "$BASE_URL" ]; then
    DOCKER_CMD="$DOCKER_CMD -u \"$BASE_URL\""
fi

if [ ! -z "$OUTPUT" ]; then
    DOCKER_CMD="$DOCKER_CMD -o \"$OUTPUT\""
fi

# Execute the command
eval $DOCKER_CMD