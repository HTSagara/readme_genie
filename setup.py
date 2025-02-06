from setuptools import find_packages, setup

setup(
    name="ReadmeGenie",
    description="A tool to generate README files effortlessly",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Henrique Sagara",
    author_email="henrique.sagara@hotmail.com",
    url="https://github.com/HTSagara/readme_genie",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "cohere>=1.2.6",
        "colorama>=0.4.6",
        "groq>=0.11.0",
        "python-dotenv>=1.0.0",
        "toml>=0.10.0",
    ],
    extras_require={
        "dev": [
            "black>=24.1.0",
            "ruff>=0.2.0",
            "pre-commit>=3.5.0",
            "coverage>=7.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "readmegenie=readmegenie.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
