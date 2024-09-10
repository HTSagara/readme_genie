
**ReadmeGenie**
================

ReadmeGenie is a Python script that uses the Groq API to generate a detailed README.md file for a given set of input files.

**Features**
-----------

* Supports multiple input files
* Allows for customization of API key, base URL, and output filename
* Saves API key and base URL to a `.env` file for future use (optional)
* Automatically generates a detailed README.md file using Groq's AI-powered text generation capabilities

**Installation**
--------------

To use ReadmeGenie, you will need to install the required libraries. You can do this by running the following command:
```bash
pip install python-dotenv groq
```
**Usage**
---------

To generate a README.md file using ReadmeGenie, simply run the script from the command line:
```bash
python readme_genie.py <file1> <file2> ...
```
Replace `<file1>`, `<file2>`, etc. with the names of the input files you want to generate a README.md file for.

**Options**
---------

You can customize the behavior of ReadmeGenie by using the following command-line options:

* `-a`, `--api-key`: Specify your Groq API key
* `-u`, `--base-url`: Specify the base URL for the Groq API
* `-o`, `--output`: Specify the output filename for the generated README.md file (default is `README.md`)
* `-v`, `--version`: Display the version number of ReadmeGenie

**Example**
----------

Here is an example of how to use ReadmeGenie to generate a README.md file for two input files:
```bash
python readme_genie.py file1.md file2.md
```
This will generate a README.md file using the content of `file1.md` and `file2.md` as input.

**Troubleshooting**
-----------------

If you encounter any issues while using ReadmeGenie, you can refer to the following troubleshooting tips:

* Make sure you have installed the required libraries (python-dotenv and groq)
* Check that your API key is valid and correct
* Verify that the input files exist and can be read
* If you encounter any errors, try running the script with the `-v` option to display more detailed output

**License**
---------

ReadmeGenie is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

**Author**
---------

ReadmeGenie was written by [Your Name]. Feel free to reach out to me if you have any questions or need further assistance.

**Version**
---------

ReadmeGenie version: 0.1

This readme file was auto-generated using Readme Genie