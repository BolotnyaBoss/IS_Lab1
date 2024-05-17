# requirements.txt
## Overview
The `requirements.txt` file is used to specify the dependencies and versions of external libraries required by the project. It is commonly used in Python projects and plays a crucial role in ensuring that all the necessary dependencies are installed for the project to run successfully.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Dependencies](#dependencies)

## Prerequisites
There are no specific prerequisites for using the `requirements.txt` file. However, it is assumed that the user has a basic understanding of Python and package management.

## Usage
To use the `requirements.txt` file in a project, follow these steps:
1. Create a new Python project or navigate to an existing one.
2. Create a file named `requirements.txt` in the root directory of the project.
3. Open the `requirements.txt` file in a text editor.
4. Copy the contents of the provided `requirements.txt` file and paste them into the `requirements.txt` file in your project.
5. Save the `requirements.txt` file.

To install the dependencies specified in the `requirements.txt` file, use the following command in the command line:
```
pip install -r requirements.txt
```
This command will install all the required libraries and their specified versions.

## Dependencies
The `requirements.txt` file lists the dependencies and their versions required for the project. Here are the dependencies specified in the provided `requirements.txt` file:

- altair==5.2.0
- attrs==23.2.0
- blinker==1.7.0
- cachetools==5.3.3
- certifi==2024.2.2
- charset-normalizer==3.3.2
- click==8.1.7
- contourpy==1.2.0
- cycler==0.12.1
- fonttools==4.50.0
- gitdb==4.0.11
- GitPython==3.1.42
- idna==3.6
- Jinja2==3.1.3
- jsonschema==4.21.1
- jsonschema-specifications==2023.12.1
- kiwisolver==1.4.5
- markdown-it-py==3.0.0
- MarkupSafe==2.1.5
- matplotlib==3.8.3
- mdurl==0.1.2
- numpy==1.26.4
- packaging==23.2
- pandas==2.2.1
- pillow==10.2.0
- protobuf==4.25.3
- pyarrow==15.0.1
- pydeck==0.8.1b0
- Pygments==2.17.2
- pyparsing==3.1.2
- python-dateutil==2.9.0.post0
- pytz==2024.1
- referencing==0.34.0
- requests==2.31.0
- rich==13.7.1
- rpds-py==0.18.0
- six==1.16.0
- smmap==5.0.1
- streamlit==1.32.2
- tenacity==8.2.3
- toml==0.10.2
- toolz==0.12.1
- tornado==6.4
- typing_extensions==4.10.0
- tzdata==2024.1
- urllib3==2.2.1

These dependencies are required by the project and will be installed when the `pip install -r requirements.txt` command is executed.