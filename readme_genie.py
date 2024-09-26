# readme_genie.py
import argparse
import sys
from models.model import generate_readme
import logging_config

# Set up the logger
logger = logging_config.setup_logger()

VERSION = "0.1"
TOOL_NAME = "ReadmeGenie"

# Custom ArgumentParser to override the error method for improved logging
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Log the error message
        logger.error(f"Argument error: {message}")
        # Show the help message
        self.print_help()
        # Exit the program with an error code
        sys.exit(1)

def main():
    try:
        parser = CustomArgumentParser(
            description="Generate a README.md file using Groq.",
            usage="%(prog)s [options] <file1> <file2> ..."
        )

        parser.add_argument("files", nargs='+', type=str, help="The input file(s) to generate the README for.")
        parser.add_argument("-a", "--api-key", type=str, help="Your Groq API key.")
        parser.add_argument("-u", "--base-url", type=str, help="The base URL for the Groq API.")
        parser.add_argument("-o", "--output", type=str, default="README.md", help="The output filename for the generated README.")
        parser.add_argument("-t", "--token-usage", action="store_true", help="Display token usage information for the request.")
        parser.add_argument("-v", "--version", action="version", version=f"{TOOL_NAME} {VERSION}")

        args = parser.parse_args()

        # Include the token_usage argument in the function call
        generate_readme(args.files, args.api_key, args.base_url, args.output, args.token_usage)

        # If everything goes well, exit with code 0 (success)
        sys.exit(0)

    except SystemExit as e:
        # Log the exit status code for debugging purposes
        if e.code != 0:
            logger.error(f"Program exited with status code {e.code}")
        sys.exit(e.code)

if __name__ == "__main__":
    main()
