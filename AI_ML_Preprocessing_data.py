"""This script demonstrates how to preprocess data using the pandas and scikit-learn libraries.
It includes steps to handle missing values, scale numerical features, and encode categorical variables.
The sample data includes age, income, and gender columns."""


import pandas as pd  # Importing the pandas library for data manipulation
from sklearn.impute import SimpleImputer  # Importing SimpleImputer for handling missing values
from sklearn.preprocessing import StandardScaler, OneHotEncoder  # Importing StandardScaler and OneHotEncoder for scaling and encoding
from sklearn.compose import ColumnTransformer  # Importing ColumnTransformer for combining preprocessing steps
from sklearn.pipeline import Pipeline  # Importing Pipeline for creating a sequence of preprocessing steps

# Define preprocessing steps
numerical_features = ['age', 'income']
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Handle missing values by imputing the mean
    ('scaler', StandardScaler())  # Scale numerical features
])

categorical_features = ['gender']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Impute missing categorical values with the most frequent value
    ('encoder', OneHotEncoder())  # One-hot encode categorical variables
])

# Combine transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),  # Apply numerical transformations
        ('cat', categorical_transformer, categorical_features)  # Apply categorical transformations
    ]
)

# Function to preprocess data
def preprocess_data(data):
    df = pd.DataFrame(data)  # Create a DataFrame from the input data
    processed_data = preprocessor.fit_transform(df.drop('target', axis=1))  # Exclude target variable and apply preprocessing
    return processed_data

if __name__ == "__main__":
    from AI_ML_sample_data import data  # Importing sample data
    processed_data = preprocess_data(data)
    print(processed_data)  # Print the processed data

# Explantation: 
    # Import Libraries: The script imports the necessary libraries, including pandas for data manipulation and scikit-learn for preprocessing.
    # Define Preprocessing Steps: The script defines the preprocessing steps for numerical and categorical features:
    # Numerical features are imputed with the mean and scaled using StandardScaler.
    # Categorical features are imputed with the most frequent value and one-hot encoded using OneHotEncoder.
    # Combine Transformations: The ColumnTransformer is used to combine the transformations for numerical and categorical features.
    # Preprocess Function: A function preprocess_data is defined to apply the preprocessing pipeline to the input data.
    # Main Execution: The script imports sample data from sample_data.py, applies the preprocessing pipeline, and prints the processed data.
    # Make sure you have the sample_data.py file in the same directory as preprocess_data.py with the following content:)
