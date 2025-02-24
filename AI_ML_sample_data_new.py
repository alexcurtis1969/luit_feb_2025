"""
Sample data for testing the data preprocessing pipeline.
This dataset includes numerical and categorical features with some missing values.
"""

import pandas as pd

# Sample data for testing
data = {
    'age': [22, 27, 35, 45, 50, None, 29, 31, None, 38],
    'income': [45000, 52000, 60000, 71000, 85000, 48000, None, 54000, 63000, None],
    'gender': ['female', 'male', 'female', 'male', 'female', 'male', None, 'female', 'male', 'female'],
    'education_level': ['bachelor', 'master', 'phd', 'highschool', 'bachelor', None, 'highschool', 'bachelor', 'master', 'phd'],
    'target': [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]  # Example target variable for binary classification
}
