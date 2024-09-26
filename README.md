**README Genie: A Tool for Generating README.md Files**

**Introduction**

Readme Genie is a command-line tool designed to generate README.md files using AI models such as Groq and Cohere. With Readme Genie, you can easily create detailed README files with introductions, how-to-uses, and examples for any project or file content.

**How to Use**

To use Readme Genie, follow these steps:

1. Install the tool by cloning the repository or downloading the executable file.
2. Run the tool using the following command:

```
python readme_genie.py
```

3. Provide the required arguments:

* `files`: One or more input files to generate the README for.
* `api-key`: Your API key for the chosen AI model (Groq or Cohere).
* `base-url`: The base URL for the chosen AI model (Groq or Cohere).
* `output`: The output filename for the generated README (default: README.md).
* `token-usage`: Show token usage information for the request (optional).
* `version`: Show the version number of the tool (optional).

Example:

```
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com file1.txt file2.txt -o my_readme.md -t
```

**Examples**

Here are some examples to illustrate how to use Readme Genie:

* Generate a README for a single file:

```
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com file.txt -o readme.md
```

* Generate a README for multiple files:

```
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com file1.txt file2.txt file3.txt -o my_readme.md
```

* Monitor token usage information:

```
python readme_genie.py -a YOUR_API_KEY -u https://api.groq.com file.txt -o readme.md -t
```

**Log Messages**

Readme Genie logs various messages during the execution process. The log messages include:

* Error messages: These are displayed in red to indicate potential errors or issues.
* Warning messages: These are displayed in yellow to indicate potential issues or anomalies.
* Informational messages: These are displayed in green to provide helpful information or updates.

By using Readme Genie, you can create high-quality README files with ease and speed. The tool is designed to be user-friendly and adaptable to different use cases.

This readme file was auto-generated using Readme Genie