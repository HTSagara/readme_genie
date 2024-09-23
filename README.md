
**ReadmeGenie**
================

**Overview**

ReadmeGenie is a command-line tool that generates detailed README.md files for your projects using the Groq API. It allows you to provide input files that contain a brief description of your project, and then uses the Groq API to generate a comprehensive README.md file.

**Installation**

To install ReadmeGenie, you can simply download the script and run it from the command line. No additional dependencies are required, as the tool uses the Groq API and Python's built-in `argparse` module.

**Usage**

To use ReadmeGenie, simply provide the input files you want to generate a README.md file for, along with any additional options you'd like to customize the output.

**New Feature**

When the -t or --token-usage flag is used, the tool will report the following information in the logs:

Prompt Tokens: The number of tokens used in the prompt (i.e., your input).
Completion Tokens: The number of tokens in the generated README.
Total Tokens: The total number of tokens used in both the prompt and the completion.
This information is useful for tracking your API usage and ensuring you're staying within token limits.


**Options**

*    parser.add_argument("files", nargs='+', type=str, help="The input file(s) to generate the README for.")
*    parser.add_argument("-a", "--api-key", type=str, help="Your Groq API key.")
*    parser.add_argument("-u", "--base-url", type=str, help="The base URL for the Groq API.")
*    parser.add_argument("-o", "--output", type=str, default="README.md", help="The output filename for the generated README.")
*    parser.add_argument("-t", "--token-usage", action="store_true", help="Display token usage information for the request.")
*    parser.add_argument("-v", "--version", action="version", version=f"{TOOL_NAME} {VERSION}")


**Example**

To generate a README.md file for a project with multiple files, use the following command:
```
python readmegenie.py -f file1.txt file2.txt -a YOUR_GROQ_API_KEY -u YOUR_GROQ_BASE_URL -o my_readme.md
```
Replace `file1.txt` and `file2.txt` with the input files you want to generate the README for, and `YOUR_GROQ_API_KEY` and `YOUR_GROQ_BASE_URL` with your Groq API key and base URL, respectively. The output filename will be `my_readme.md`.

**How it Works**

When you run ReadmeGenie, it follows these steps:

1. It checks if the input files exist and are readable.
2. It loads the Groq API key from a `.env` file or an environment variable, and sets up the Groq API client.
3. It concatenates the content of the input files and makes a request to the Groq API to generate a README.md file.
4. It saves the generated README.md file to the output filename specified by the user.



**License**

ReadmeGenie is released under the MIT License. See the LICENSE file for more information.

**Contributing**

If you'd like to contribute to ReadmeGenie, please fork the repository and submit a pull request with your changes.

This readme file was auto-generated using Readme Genie