# main.py
## Overview
The `main.py` file is a Python script that implements a user interface for analyzing the fit between candidates and roles in a software project. It utilizes the `streamlit` library for creating the user interface and performs calculations using `numpy`, `pandas`, and `matplotlib` libraries. The purpose of this script is to enable users to select a methodology and input candidate scores and role requirements, and then visualize the fit between candidates and roles using various charts and diagrams.
## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Methods](#methods)
4. [Useful details](#properties)
## Prerequisites
This script requires the following dependencies:
- streamlit
- numpy
- pandas
- matplotlib
## Usage
To use this script in a project, follow these steps:
1. Install the required dependencies using the package manager of your choice.
2. Create a new Python file and import the necessary libraries:
```python
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
3. Copy the code from `main.py` into your file.
4. Customize the code as needed for your project.
5. Run the Python script and access the user interface through your web browser.
6. Select a methodology, input candidate scores and role requirements, and visualize the fit between candidates and roles using the provided charts and diagrams.
## Methods
This script defines the following methods:
### `max_min_composition(candidate, roles)`
This method takes a candidate score matrix and role requirement matrix as input and returns the maximum of the minimum scores for each candidate and role combination.
- `candidate` (numpy.ndarray): The candidate score matrix.
- `roles` (numpy.ndarray): The role requirement matrix.
- Returns: The maximum of the minimum scores for each candidate and role combination.

Example usage:
```python
max_min_scores = max_min_composition(candidate_scores, role_requirements)
```
## Useful details
- The `methodologies` dictionary defines the available methodologies, each with its corresponding matrix and role names.
- The `candidate_scores_default` and `candidate_scores_default_dsms` arrays provide example candidate scores for different methodologies.
- The user interface allows the user to select a methodology, input candidate scores, and view the fit between candidates and roles using various charts and diagrams.
- The user interface is built using the `streamlit` library.
- The charts and diagrams are created using the `matplotlib` library.