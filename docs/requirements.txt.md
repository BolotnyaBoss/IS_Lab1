# requirements.txt
## Overview
The `requirements.txt` file lists all the external libraries and dependencies that are required for the project. It specifies the versions of each library that should be installed in order to run the project successfully. This file plays a crucial role in managing the project's dependencies and ensuring that all the required libraries are installed.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Methods](#methods)
4. [Useful details](#useful-details)

## Prerequisites
There are no specific prerequisites for the `requirements.txt` file itself. However, in order to use the libraries listed in the file, the user should have a compatible version of Python installed on their system.

## Usage
To use the `requirements.txt` file in a project, follow the steps below:

1. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv myenv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```shell
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```shell
     source myenv/bin/activate
     ```

3. Install the required libraries using pip:
   ```shell
   pip install -r requirements.txt
   ```

## Methods
There are no methods or functions in the `requirements.txt` file. It consists of a list of external libraries and their versions, each specified in the format `library_name==version_number`. These libraries are used by the project for various purposes such as data manipulation, plotting, web requests, etc.

Here are some examples of libraries listed in the `requirements.txt` file:

- `pandas==2.2.1`: A powerful data manipulation library used for data analysis and manipulation.
- `matplotlib==3.8.3`: A plotting library used for creating visualizations.
- `requests==2.31.0`: A library used for making HTTP requests.
- `streamlit==1.32.2`: A library used for building interactive web applications.

The specific methods and functions provided by each library can be found in their respective documentation.

## Useful details
- The `==` operator in the `requirements.txt` file specifies the exact version of the library that should be installed. If a different version is installed, it may lead to compatibility issues.
- It is recommended to periodically update the `requirements.txt` file to include the latest versions of the libraries used in the project. This ensures that the project stays up to date with the latest features and bug fixes.
- The `requirements.txt` file can be generated automatically using tools like `pip freeze`, which scans the currently installed libraries and generates a `requirements.txt` file with their versions. This makes it easier to share the project's dependencies with others.