================================

Introduction
-----------

ReadmeGenie is a Python script that generates a markdown README file using Groq and Cohere APIs. With ReadmeGenie, you can create a detailed README file with introduction, how-to-use, and examples for your software or project in just a few steps.

Getting Started
---------------

### Installation

To install ReadmeGenie, simply clone this repository and run the script.

```bash
git clone https://github.com/your-username/ReadmeGenie.git
cd ReadmeGenie
python readme_genie.py
```

### Usage

To use ReadmeGenie, you will need to provide the input file(s) to generate the README for, as well as the optional API key and base URL for Groq or Cohere.

```bash
python readme_genie.py -a <api_key> -u <base_url> file1.md file2.md ...
```

### Options

*   `-a`, `--api-key`: Your Groq or Cohere API key.
*   `-u`, `--base-url`: The base URL for the Groq or Cohere API.
*   `file1.md`, `file2.md`, ...: The input file(s) to generate the README for.
*   `-o`, `--output`: The output filename for the generated README (default: README.md).
*   `-t`, `--token-usage`: Display token usage information for the request.
*   `-v`, `--version`: Display the version number of ReadmeGenie.

Examples
-------

### Simple Usage

Generate a README file for a single input file:

```bash
python readme_genie.py -a <api_key> -u <base_url> file.md
```

### Advanced Usage

Generate a README file for multiple input files and display token usage information:

```bash
python readme_genie.py -a <api_key> -u <base_url> file1.md file2.md -t
```

License
------

ReadmeGenie is licensed under the MIT License. See `LICENSE` for details.

Contributing
------------

If you'd like to contribute to ReadmeGenie, please see `CONTRIBUTING.md` for guidelines.

Author
------

ReadmeGenie was created by [Your Name](https://github.com/your-username).

This readme file was auto-generated using Readme Genie