"""Sample data for testing the data preprocessing pipeline.
This dataset includes numerical and categorical features with some missing values."""


import pandas as pd

# Sample data for testing
data = {
    'age': [25, 30, 35, None, 40, 28, 33, None, 45, 29],
    'income': [50000, 60000, 70000, 80000, None, 55000, 68000, None, 72000, 64000],
    'gender': ['male', 'female', 'female', 'male', 'female', None, 'male', 'female', 'male', 'female'],
    'target': [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]  # Example target variable for binary classification
}
