
**ReadmeGenie**
================

**Version:** `0.1`

**Description:**
ReadmeGenie is a tool that uses the Groq API to generate a detailed README.md file for a given set of files. It allows you to provide an API key, base URL, and output filename to customize the generation process.

**Usage:**
To use ReadmeGenie, simply run the command with the following options:

* `--files` or `-f`: One or more input files to generate the README for. These files will be concatenated and used as the content for the README.
* `--api-key` or `-a`: Your Groq API key. This can be provided as an argument or as an environment variable named `GROQ_API_KEY`.
* `--base-url` or `-u`: The base URL for the Groq API. This can be provided as an argument or as an environment variable named `GROQ_BASE_URL`.
* `--output` or `-o`: The output filename for the generated README. Default is `README.md`.
* `--version` or `-v`: Display the version of ReadmeGenie.

Example usage:

```
python readme_genie.py file1.md file2.md -a YOUR_API_KEY -u https://api.groq.com -o README-generated.md
```

**How it works:**
ReadmeGenie uses the Groq API to generate a detailed README.md file based on the provided files. It checks if the API key is provided as an argument or as an environment variable, and if not, it prompts the user to save it in a `.env` file for future use. The tool also allows the user to update the `.env` file if they provide a different API key.

**Error handling:**
ReadmeGenie can handle unexpected errors and display the error message to the user.

**Environment variables:**
ReadmeGenie uses the following environment variables:

* `GROQ_API_KEY`: Your Groq API key (optional)
* `GROQ_BASE_URL`: The base URL for the Groq API (optional)

**Note:** You need to have the Groq API key and base URL to use this tool. The `.env` file is used to store these values for future use.

**License:**
ReadmeGenie is released under the [MIT License](https://opensource.org/licenses/MIT).

**Disclaimer:**
This tool is developed and maintained by [Your Name]. Use at your own risk.

This readme file was auto-generated using Readme Genie