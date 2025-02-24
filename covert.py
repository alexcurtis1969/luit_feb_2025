"""This script demonstrates how to preprocess data using the pandas and scikit-learn libraries.
It includes steps to handle missing values, scale numerical features, and encode categorical variables.
The sample data includes age, income, and gender columns."""

import pandas as pd  # Importing the pandas library for data manipulation
from sklearn.impute import SimpleImputer  # Importing SimpleImputer for handling missing values
from sklearn.preprocessing import StandardScaler, OneHotEncoder  # Importing StandardScaler and OneHotEncoder for scaling and encoding
from sklearn.compose import ColumnTransformer  # Importing ColumnTransformer for combining preprocessing steps
from sklearn.pipeline import Pipeline  # Importing Pipeline for creating a sequence of preprocessing steps

# Sample data for testing
data = {
    'age': [25, 30, 35, None, 40, 28, 33, None, 45, 29],
    'income': [50000, 60000, 70000, 80000, None, 55000, 68000, None, 72000, 64000],
    'gender': ['male', 'female', 'female', 'male', 'female', None, 'male', 'female', 'male', 'female'],
    'target': [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]  # Example target variable for binary classification
}

# Define preprocessing steps
numerical_features = ['age', 'income']
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Handle missing values by replacing with the mean
    ('scaler', StandardScaler())  # Scale numerical features
])

categorical_features = ['gender']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values by replacing with the most frequent value
    ('encoder', OneHotEncoder())  # Encode categorical variables using one-hot encoding
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
    df = pd.DataFrame(data)  # Convert data to a DataFrame
    processed_data = preprocessor.fit_transform(df.drop('target', axis=1))  # Exclude target variable and apply preprocessing
    return processed_data

if __name__ == "__main__":
    processed_data = preprocess_data(data)  # Preprocess the sample data
    
    # Convert the NumPy array to a DataFrame with appropriate column names
    new_columns = ['age_scaled', 'income_scaled', 'gender_female', 'gender_male', 'gender_none']
    processed_df = pd.DataFrame(processed_data, columns=new_columns)
    
    # Display the DataFrame
    print(processed_df)
