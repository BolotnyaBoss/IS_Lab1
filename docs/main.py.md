# main.py
## Overview
The `main.py` file is a Python script that provides a user interface for analyzing the suitability of candidates for roles in a project based on their competency scores. It uses various methodologies such as MSF, XP, DSMS, and OpenUP to calculate the maximum-minimum scores for each candidate and role. The script also generates visualizations such as histograms, line charts, and pie charts to represent the scores.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Methods](#methods)
4. [Useful details](#properties)

## Prerequisites
- Python 3.x
- Streamlit
- NumPy
- pandas
- matplotlib

## Usage
To use the `main.py` file in a project, follow these steps:
1. Install the required dependencies by running:
   ```
   pip install streamlit numpy pandas matplotlib
   ```
2. Create a file named `data.py` in the same directory as `main.py` and define the required data structures (`msf_matrix`, `msf_roles`, etc.). Refer to the example code in the script for reference.
3. Run the script using the following command:
   ```
   streamlit run main.py
   ```
4. Access the user interface in a web browser by opening the provided URL.

## Methods
- `max_min_composition(candidate, roles)`: Calculates the maximum-minimum scores for each candidate and role based on their competency scores. Takes two parameters:
  - `candidate`: a NumPy array representing the competency scores of the candidates. Each row represents a candidate, and each column represents a competency.
  - `roles`: a NumPy array representing the role requirements. Each row represents a role, and each column represents a competency.
  Returns a NumPy array containing the maximum-minimum scores for each candidate and role.

## Useful details
- The `methodologies` dictionary contains the matrices and role names for various methodologies.
- The script uses the Streamlit library to create a web-based user interface.
- The user can select a methodology and input candidate competency scores.
- The script then calculates the maximum-minimum scores and generates visualizations to represent the results.