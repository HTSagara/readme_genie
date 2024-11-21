# readme_genie.py
import argparse
import sys

from src import logging_config
from src.loadConfig import load_config
from src.models.model import (
    handle_api_request,
    process_and_save_readme,
    read_file_content,
)

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


def parse_arguments(config):
    parser = CustomArgumentParser(
        description="Generate a README.md file using Groq or Cohere.",
        usage="%(prog)s [options] <file1> <file2> ...",
    )
    parser.add_argument(
        "files",
        nargs="+",
        type=str,
        help="Input file(s) to generate the README.",
    )
    parser.add_argument(
        "-a",
        "--api-key",
        type=str,
        help="Your API key.",
        default=config.get("api_key"),
    )
    parser.add_argument(
        "-u",
        "--base-url",
        type=str,
        help="The base URL.",
        default=config.get("base_url"),
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output filename for the generated README.",
        default=config.get("output", "README.md"),
    )
    parser.add_argument(
        "-t",
        "--token-usage",
        action="store_true",
        help="Display token usage.",
        default=config.get("token_usage", False),
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{TOOL_NAME} {VERSION}"
    )
    return parser.parse_args()


def main():
    try:
        # Load config file
        config = load_config()

        args = parse_arguments(config)

        file_content = read_file_content(args.files)
        response = handle_api_request(
            args.api_key, args.base_url, file_content
        )
        output_filename = args.output or "README.md"

        # Include the token_usage argument in the function call
        process_and_save_readme(response, output_filename, args.token_usage)

        # If everything goes well, exit with code 0 (success)
        sys.exit(0)

    except SystemExit as e:
        # Log the exit status code for debugging purposes
        if e.code != 0:
            logger.error(f"Program exited with status code {e.code}")
        sys.exit(e.code)


if __name__ == "__main__":
    main()
