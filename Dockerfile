# Use the official Python 3.12 image from Docker Hub
FROM python:3.12.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure readme_genie.py is executable
RUN chmod +x readme_genie.py

# Set the default command to run the application using Python
CMD ["python3", "/app/readme_genie.py"]
