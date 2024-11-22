from setuptools import find_packages, setup

setup(
    name="ReadmeGenie",
    use_scm_version=True,  # Use setuptools_scm for versioning
    setup_requires=["setuptools_scm"],  # Ensure setuptools_scm is installed
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
        "cohere==5.11.0",
        "colorama==0.4.6",
        "groq==0.11.0",
        "python-dotenv==1.0.1",
        "toml==0.10.2",
        "black==23.3.0",
        "ruff==0.0.261",
        "pre-commit",
        "coverage",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
