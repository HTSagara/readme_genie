import os
import argparse
import json
from dotenv import load_dotenv
from groq import Groq
import logging_config
from colorama import Fore, Style

VERSION = "0.1"
TOOL_NAME = "ReadmeGenie"
FOOTER_STRING = "\n\nThis readme file was auto-generated using Readme Genie"

# Set up the logger from logging_config
logger = logging_config.setup_logger()

def get_env():
    return os.path.isfile('.env')

def create_env(api_key, base_url):
    with open('.env', 'w') as env_file:
        env_file.write(f"GROQ_API_KEY={api_key}\n")
        env_file.write(f"GROQ_BASE_URL={base_url}\n")

def generate_readme(file_paths, api_key, base_url, output_filename):
    try:
        load_dotenv()

        # Check if the api_key was provided either as an environment variable or as an argument
        if not api_key and not get_env():
            raise Exception("Please provide an API_KEY")

        # Get the base_url from arguments, environment, or use the default
        if not base_url:
            base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com")

        client = Groq(
            api_key=api_key or os.getenv("GROQ_API_KEY"), 
            base_url=base_url
        )

        # Concatenate content from multiple files
        file_content = ""
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                file_content += file.read() + "\n\n"

        # Make a request to Groq
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"Generate a detailed README.md file for the following file content:\n\n{file_content}"}
            ],
            model="llama3-8b-8192",
        )
        readme_content = response.choices[0].message.content.strip() + FOOTER_STRING
        
        # Checks if the content starts with the title
        if readme_content[0] != '*':
            # print("\n".join(readme_content.split('\n')[1:]))
            readme_content = "\n".join(readme_content.split('\n')[1:])


        # Save to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(readme_content)
        logger.info(f"README.md file generated and saved as {output_filename}")
        logger.info(f"This is your file's content:\n {readme_content}")

        # If there is no .env file, the user can choose to save it for future use
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

    except Exception as e:
        # Log other unexpected errors
        logger.error(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a README.md file using Groq.",
        usage="%(prog)s [options] <file1> <file2> ...",
    )

    parser.add_argument("files", nargs='+', type=str, help="The input file(s) to generate the README for.")
    parser.add_argument("-a", "--api-key", type=str, help="Your Groq API key.")
    parser.add_argument("-u", "--base-url", type=str, help="The base URL for the Groq API.")
    parser.add_argument("-o", "--output", type=str, default="README.md", help="The output filename for the generated README.")
    parser.add_argument("-v", "--version", action="version", version=f"{TOOL_NAME} {VERSION}")

    args = parser.parse_args()

    generate_readme(args.files, args.api_key, args.base_url, args.output)

if __name__ == "__main__":
    main()
