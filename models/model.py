# models/model.py
import os
import sys

import logging_config
from models.cohere_api import cohereAPI
from models.groq_api import groqAPI

FOOTER_STRING = "\n\nThis readme file was auto-generated using Readme Genie"

# Set up the logger from logging_config
logger = logging_config.setup_logger()


def get_env():
    return os.path.isfile(".env")


def create_env(api_key, base_url, model):
    with open(".env", "a") as env_file:
        if model == "cohere":
            env_file.write(f"COHERE_API_KEY={api_key}\n")
            env_file.write(f"COHERE_BASE_URL={base_url}\n")
        else:
            env_file.write(f"GROQ_API_KEY={api_key}\n")
            env_file.write(f"GROQ_BASE_URL={base_url}\n")


def selectModel(base_url):
    # If the user specifies the base url to use cohere
    if base_url == "https://api.cohere.ai/v1":
        return "cohere"
    # Otherwise, it will use groq by default
    else:
        return "groq"


def read_file_content(file_paths):
    file_content = ""
    try:
        for file_path in file_paths:
            with open(file_path, "r") as file:
                file_content += file.read() + "\n\n"
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        sys.exit(1)
    return file_content


def handle_api_request(api_key, base_url, file_content):
    chosen_model = selectModel(base_url)
    if chosen_model == "cohere":
        response = cohereAPI(api_key, file_content)
    else:
        response = groqAPI(api_key, base_url, file_content)
    return response


def check_title(readme_content):
    if readme_content[0] != "*":
        readme_content = "\n".join(readme_content.split("\n")[1:])
    return readme_content


def process_and_save_readme(response, output_filename, token_usage):
    try:
        # Check if the response is from Groq or Cohere and extract content accordingly
        if hasattr(response, "choices"):  # Groq API response
            readme_content = response.choices[0].message.content.strip()
        elif hasattr(response, "generations"):  # Cohere API response
            readme_content = response.generations[0].text.strip()
        else:
            logger.error("Unknown response structure")
            sys.exit(1)

        final_content = check_title(readme_content)
        # Save the README content to a file
        with open(output_filename, "w") as output_file:
            output_file.write(final_content)
        logger.info(f"README.md file generated and saved as {output_filename}")
        logger.warning(f"This is your file's content:\n{final_content}")

        if token_usage:
            report_token_usage(response)
    except Exception as e:
        logger.error(f"Error processing and saving README: {e}")
        sys.exit(1)


def report_token_usage(response):
    try:
        usage = response.usage
        logger.info(
            f"Token Usage Information: Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}"
        )
    except AttributeError:
        logger.warning(
            "Token usage information not available for this response."
        )
