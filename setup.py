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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
