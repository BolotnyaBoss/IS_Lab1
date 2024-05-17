# main.py
## Overview
The `main.py` file is a script that provides a user interface for analyzing the fit between candidates and roles in a software project. It allows the user to select a methodology, input candidate scores, and view the maximum-minimum scores of the candidate's fit to each role. It also provides visualizations of the scores, including a histogram, line chart, and pie chart.

This script plays a role in a larger software project by providing a tool for evaluating the suitability of candidates for different roles in the project. It uses data from the `data.py` module to define the role requirements for each methodology.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Methods](#methods)
4. [Useful details](#properties)

## Prerequisites
This script has the following dependencies:
- streamlit
- numpy
- pandas
- matplotlib

These dependencies can be installed using the following command:
```
pip install streamlit numpy pandas matplotlib
```

## Usage
To use this script, follow these steps:
1. Install the required dependencies as mentioned in the prerequisites section.
2. Run the script using the following command:
   ```
   streamlit run main.py
   ```
3. Access the script's user interface through a web browser at the provided URL.

## Methods
### `max_min_composition(candidate, roles)`
This method calculates the maximum-minimum scores for a candidate's fit to each role. It takes two parameters:
- `candidate`: A NumPy array containing the candidate's scores for each competency.
- `roles`: A NumPy array containing the role requirements for each competency.

```python
def max_min_composition(candidate, roles):
    min_scores = np.minimum(candidate[:, np.newaxis, :], roles[np.newaxis, :, :])
    max_min_scores = np.max(min_scores, axis=2)
    return max_min_scores
```

## Useful details
- The `methodologies` dictionary defines the role requirements and names for each methodology.
- The `candidate_scores_default` and `candidate_scores_default_dsms` variables contain example candidate scores for different methodologies.
- The script uses the Streamlit library to create a user interface.
- The script generates visualizations using the Matplotlib library.