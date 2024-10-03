#!/bin/bash
docker run --rm -v "$(pwd)":/app readmegenie:latest python3 readme_genie.py "$@"