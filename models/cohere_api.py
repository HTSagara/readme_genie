# models/cohere_api.py
import cohere
from dotenv import load_dotenv
import logging_config
import os

# Set up the logger from logging_config
logger = logging_config.setup_logger()

def get_env():
    return os.path.isfile('.env')

def cohereAPI(api_key, file_content):
    load_dotenv()

    client = cohere.Client(
            api_key or os.getenv("COHERE_API_KEY")
        )

    response = client.generate(
        prompt=f"Generate a detailed README.md with introduction, how-to-use, and examples for the following file content:\n\n{file_content}"
    )
    logger.info(f"Response from the API using COHERE API")
    logger.info(f"{response}")
    
    return response