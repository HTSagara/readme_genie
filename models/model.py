# models/model.py
from dotenv import load_dotenv
from groq import Groq
import logging_config
import os
from colorama import Fore, Style
from models.groq_api import groqAPI
from models.cohere_api import cohereAPI


FOOTER_STRING = "\n\nThis readme file was auto-generated using Readme Genie"

# Set up the logger from logging_config
logger = logging_config.setup_logger()

def get_env():
    return os.path.isfile('.env')

def create_env(api_key, base_url):
    with open('.env', 'w') as env_file:
        env_file.write(f"GROQ_API_KEY={api_key}\n")
        env_file.write(f"GROQ_BASE_URL={base_url}\n")

def selectModel(base_url):
    # If the user specifies the base url to use cohere
    if base_url == 'https://api.cohere.ai/v1':
        return 'cohere'
    # Otherwise, it will use groq by default
    else:
        return 'groq'

def generate_readme(file_paths, api_key, base_url, output_filename, token_usage):
    try:
        load_dotenv()

        # Check if the api_key was provided either as an environment variable or as an argument
        if not api_key and not get_env():
            raise Exception("Please provide an API_KEY")
        
        # Concatenate content from multiple files
        file_content = ""
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                file_content += file.read() + "\\n\\n"

        # Get the base_url from arguments, environment, or use the default
        chosenModel = selectModel(base_url)
        if chosenModel == 'cohere':
            base_url = os.getenv("COHERE_BASE_URL", "https://api.cohere.ai/v1")
            response = cohereAPI(api_key, base_url, file_content)
            readme_content = response.generations[0].text.strip() + FOOTER_STRING
        else:
            base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com")
            response = groqAPI(api_key, base_url, file_content)
            readme_content = response.choices[0].message.content.strip() + FOOTER_STRING
        
        if readme_content[0] != '*':
            readme_content = "\n".join(readme_content.split('\n')[1:])
        
        with open(output_filename, 'w') as output_file:
            output_file.write(readme_content)
        logger.info(f"README.md file generated and saved as {output_filename}")
        logger.info(f"This is your file's content:\\n {readme_content}")

        if not get_env() and api_key is not None:
            logger.info("Would you like to save your API key and base URL in a .env file for future use? [y/n]")
            answer = input()
            if answer.lower() == 'y':
                create_env(api_key, base_url)
        # If the user provides an API_KEY different from the saved one
        elif get_env() and api_key != os.getenv("GROQ_API_KEY"):
            if api_key is not None:
                logger.info("You entered a different API key. Would you like to update your .env file? [y/n]")
                answer = input()
                if answer.lower() == 'y':
                    create_env(api_key, base_url)

        # Report token usage if the flag is set
        # Correct usage access
        if token_usage:
            usage = response.usage  # Access the usage object using dot notation
            logger.info(f"Token Usage Information: Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}")



    except Exception as e:
        # Log other unexpected errors
        logger.error(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")