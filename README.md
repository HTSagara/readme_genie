**README.md Generation Tool - ReadmeGenie**
================================================

ReadmeGenie is a command-line tool that helps you generate README.md files for your projects. It uses natural language processing (NLP) models from Groq and Cohere to create readable and informative README files. This tool is especially useful for projects with complex codebases or documentation.

**How to Use**
-------------

To use ReadmeGenie, you need to have the following installed:

* Python 3.8 or later
* Groq API keys (free and paid options available)
* Cohere API keys (free and paid options available)

Here's a step-by-step guide to generate a README.md file:

1. Save your project files in a directory and navigate to that directory in your terminal.
2. Run the following command: `python readme_genie.py -a <api_key> -u <base_url> -o output_file.md <input_file1> <input_file2> ...`

Replace:

* `<api_key>` with your Groq or Cohere API key
* `<base_url>` with the base URL for your Groq or Cohere API (e.g., `https://api.groq.com` or `https://api.cohere.ai/v1`)
* `<output_file>` with the desired output filename (default is `README.md`)
* `<input_file>` with the file(s) you want to generate the README for

Example: `python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com -o output_file.md input_file1.md input_file2.txt`

**Options**
---------

* `-a` or `--api-key`: Your Groq or Cohere API key
* `-u` or `--base-url`: The base URL for your Groq or Cohere API
* `-o` or `--output`: The output filename for the generated README (default is `README.md`)
* `--token-usage`: Display token usage information for the request
* `-v` or `--version`: Display the version of ReadmeGenie

**Examples**
------------

Here are some examples of how you can use ReadmeGenie:

1. Generate a README.md file for multiple input files:
```bash
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com -o output_file.md input_file1.md input_file2.txt input_file3.md
```
2. Generate a README.md file for a single input file with token usage information:
```bash
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com -o output_file.md -t input_file.md
```
**Tips and Tricks**
-------------------

* Make sure to save your API keys and base URLs securely, as they can be used to generate reads from your projects.
* ReadmeGenie uses the default model for generating README files. You can experiment with different models and settings to achieve better results.
* You can also customize the README templates to fit your project's style and tone.

**Troubleshooting**
-------------------

* If you encounter any issues while running ReadmeGenie, check the logs for error messages and try searching for solutions online.
* If you need help with setting up your API keys or base URLs, refer to the documentation for Groq and Cohere.

We hope you find ReadmeGenie useful for generating high-quality README files for your projects!

This readme file was auto-generated using Readme Genie