# main.py
## Overview
The `main.py` file is a part of a software project that aims to analyze the fit of candidates for different roles in a project based on their competencies. It provides a user interface using the Streamlit library to input candidate scores and role requirements, and then calculates and visualizes the matching scores.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Methods](#methods)
4. [Useful details](#properties)

## Prerequisites
This file has the following dependencies:
- `streamlit` library
- `numpy` library
- `pandas` library
- `matplotlib` library

## Usage
To use this file in a project, follow these steps:
1. Install the required dependencies using the appropriate package manager.
2. Import the necessary libraries:
```python
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
3. Provide the necessary data inputs:
- `methodologies`: a dictionary containing different methodologies and their corresponding matrices and role names.
- `candidate_scores_default` and `candidate_scores_default_dsms`: default candidate scores for different methodologies.

4. Utilize the provided methods and functions as needed:
- `max_min_composition(candidate, roles)`: calculates the maximum of the minimum scores for each candidate based on the roles.
- User interface: Uses the Streamlit library to create a user interface for selecting the methodology, inputting candidate scores and role requirements, and displaying the matching scores using various visualizations.

## Methods
This file contains the following methods and functions:
1. `max_min_composition(candidate, roles)`: Calculates the maximum of the minimum scores for each candidate based on the roles.
   - Parameters:
     - `candidate`: The candidate scores. (numpy array)
     - `roles`: The role requirements matrix. (numpy array)
   - Returns:
     - `max_min_scores`: The maximum of the minimum scores for each candidate based on the roles. (numpy array)

## Useful details
- The provided code is a part of a larger project and may require additional files and dependencies.
- The user interface is created using the Streamlit library, enabling easy interaction with the program.
- The code includes examples of default candidate scores for different methodologies (`candidate_scores_default` and `candidate_scores_default_dsms`).
- The matching scores are visualized using various plots, including a bar chart, line chart, and pie chart.