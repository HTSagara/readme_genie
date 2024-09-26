# models/model.py
from dotenv import load_dotenv
from groq import Groq, AuthenticationError
import logging_config
import os
import sys
from colorama import Fore, Style
from models.groq_api import groqAPI
from models.cohere_api import cohereAPI
from colorama import Fore, Style, init


FOOTER_STRING = "\n\nThis readme file was auto-generated using Readme Genie"

# Set up the logger from logging_config
logger = logging_config.setup_logger()

def get_env():
    return os.path.isfile('.env')

def create_env(api_key, base_url, model):
    with open('.env', 'a') as env_file:
        if model == 'cohere':
            env_file.write(f"COHERE_API_KEY={api_key}\n")
            env_file.write(f"COHERE_BASE_URL={base_url}\n")
        else:
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
            logger.error(f"{Fore.RED}API key is required but not provided. Exiting.{Style.RESET_ALL}")
            sys.exit(1)
        
        # Concatenate content from multiple files
        file_content = ""
        try:
            for file_path in file_paths:
                with open(file_path, 'r') as file:
                    file_content += file.read() + "\\n\\n"
        except FileNotFoundError as fnf_error:
            logger.error(f"{Fore.RED}File not found: {file_path}{Style.RESET_ALL}")
            sys.exit(1)
            
        # Get the base_url from arguments, environment, or use the default
        chosenModel = selectModel(base_url)
        try:
            if chosenModel == 'cohere':
                base_url = os.getenv("COHERE_BASE_URL", "https://api.cohere.ai/v1")
                response = cohereAPI(api_key, file_content)
                readme_content = response.generations[0].text.strip() + FOOTER_STRING
            else:
                base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com")
                response = groqAPI(api_key, base_url, file_content)
                readme_content = response.choices[0].message.content.strip() + FOOTER_STRING
        except AuthenticationError as auth_error:
            logger.error(f"{Fore.RED}Authentication failed: Invalid API key. Please check your API key and try again.{Style.RESET_ALL}")
            sys.exit(1)
        except Exception as api_error:
            logger.error(f"{Fore.RED}API request failed: {api_error}{Style.RESET_ALL}")
            sys.exit(1)
        
        # Process and save the generated README content
        if readme_content[0] != '*':
            readme_content = "\n".join(readme_content.split('\n')[1:])
        
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(readme_content)
            logger.info(f"README.md file generated and saved as {output_filename}")
            logger.warning(f"This is your file's content:\n{readme_content}")
        except IOError as io_error:
            logger.error(f"{Fore.RED}Failed to write to output file: {output_filename}. Error: {io_error}{Style.RESET_ALL}")
            sys.exit(1)

        # Save API key if needed
        if not get_env() and api_key is not None:
            logger.warning("Would you like to save your API key and base URL in a .env file for future use? [y/n]")
            answer = input()
            if answer.lower() == 'y':
                create_env(api_key, base_url, chosenModel)
        elif get_env():
            if chosenModel == 'cohere' and api_key != os.getenv("COHERE_API_KEY"):
                if api_key is not None:
                    logger.warning("Would you like to save this API Key? [y/n]")
                    answer = input()
                    if answer.lower() == 'y':
                        create_env(api_key, base_url, chosenModel)
            elif chosenModel == 'groq' and api_key != os.getenv("GROQ_API_KEY"):
                if api_key is not None:
                    logger.warning("Would you like to save this API Key? [y/n]")
                    answer = input()
                    if answer.lower() == 'y':
                        create_env(api_key, base_url, chosenModel)

        # Report token usage if the flag is set
        if token_usage:
            try:
                usage = response.usage
                logger.info(f"Token Usage Information: Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}")
            except AttributeError:
                logger.warning(f"{Fore.YELLOW}Token usage information is not available for this response.{Style.RESET_ALL}")

    except Exception as e:
        # Catch-all for other unexpected errors
        logger.error(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)