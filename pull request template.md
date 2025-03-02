# Pull Request Template

## Description

This pull request adds a Python script to predict house prices using a **Linear Regression** model. The script loads data from a CSV file, preprocesses the features, splits the dataset into training and testing sets, trains a linear regression model, evaluates the model's performance, and visualizes the results. Additionally, it predicts the price of a new house based on input features.

## Features Added

- **Data Loading**: Loads house price data from a CSV file.
- **Preprocessing**: Extracts features (number of rooms, size) and target variable (price).
- **Model Training**: Uses **Linear Regression** to train the model.
- **Model Evaluation**: Evaluates the model using metrics like MSE, RMSE, and R².
- **Visualization**: Plots actual data and regression line for better visualization.
- **Prediction**: Allows predicting house prices for new input data.

## How to Test

1. Clone this repository to your local machine.
2. Install required dependencies:

   ```bash
   pip install numpy pandas matplotlib scikit-learn
