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
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_features = ['gender']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder())
])

# Combine transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Function to preprocess data
def preprocess_data(data):
    df = pd.DataFrame(data)
    processed_data = preprocessor.fit_transform(df.drop('target', axis=1))  # Exclude target variable
    return processed_data

if __name__ == "__main__":
    from AI_ML_sample_data import data  # Importing sample data
    processed_data = preprocess_data(data)
    print(processed_data)
