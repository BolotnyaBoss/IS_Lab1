# requirements.txt

## Overview
The `requirements.txt` file is used to specify the dependencies and their respective versions for a software project. It lists the libraries and packages that need to be installed in order for the project to run successfully.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Dependencies](#dependencies)

## Prerequisites
There are no specific prerequisites for using the `requirements.txt` file. However, it is assumed that the user has a basic understanding of Python and package management.

## Usage
To use the `requirements.txt` file in a project, follow these steps:
1. Create a virtual environment for your project (optional but recommended).
2. Navigate to the project directory in your terminal or command prompt.
3. Run the following command to install the dependencies listed in the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```
   This command will install all the required libraries with their specified versions.

## Dependencies
The `requirements.txt` file lists the following dependencies and their respective versions:

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

These dependencies are required by the project and will be installed when running `pip install -r requirements.txt`.