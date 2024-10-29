# models/groq_api.py
import os

from dotenv import load_dotenv
from groq import Groq

import logging_config

# Set up the logger from logging_config
logger = logging_config.setup_logger()


def groqAPI(api_key, base_url, file_content):
    load_dotenv()

    client = Groq(api_key=api_key or os.getenv("GROQ_API_KEY"), base_url=base_url)

    # Make a request to Groq with the model parameter
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate a detailed README.md with introduction, how-to-use, and examples for the following file content:\n\n{file_content}",
            }
        ],
        model="llama3-8b-8192",
    )
    logger.info("Response from the API using GROQ API")
    logger.info(f"{response}")

    return response
