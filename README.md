# **Readme Genie**

Welcome to **Readme Genie**, a Python script designed to automatically generate a detailed `README.md` file with an introduction, usage instructions, and examples based on the provided file content.

## Output

The script generates a detailed `README.md` file containing:

- An introduction.
- Usage instructions.
- Examples based on the provided file content.

The file is saved under the specified output filename (e.g., `README.md`).

## Additional Notes

- Ensure the input files and API keys are correctly set up before running the script.
- You can customize the generated README by modifying the input files' content.
- Use the `setuptools` package in your `requirements.txt` to avoid environment-related issues.

## Using the `generate-readme.sh` Script

The `generate-readme.sh` script is a convenience wrapper for running the Docker container. Use it as follows:

```bash
./generate-readme.sh -a your_api_key -u https://api.groq.com -o README.md path/to/file1.py path/to/file2.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

**Readme Genie** uses:

- The official Python 3.12 Docker image.
- The Groq and Cohere APIs for generating README content.

This README was auto-generated using **Readme Genie**.
