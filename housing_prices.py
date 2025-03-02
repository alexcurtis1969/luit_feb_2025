# Import necessary libraries
import numpy as np  # For numerical operations (e.g., for calculating RMSE)
import pandas as pd  # For data manipulation (e.g., loading data from CSV)
import matplotlib.pyplot as plt  # For visualizing the data
from sklearn.linear_model import LinearRegression  # For the linear regression model
from sklearn.model_selection import train_test_split  # For splitting data into train and test sets
from sklearn.metrics import mean_squared_error, r2_score  # For evaluating model performance

# Step 1: Load data from a CSV file
# Replace 'house_prices.csv' with the actual path to your dataset
data = pd.read_csv('house_prices.csv')  # Load the dataset from CSV into a pandas DataFrame

# Step 2: Inspect the first few rows of the dataset to ensure it's loaded correctly
print(data.head())  # Print the first 5 rows of the dataset to check its structure

# Step 3: Extract features and target variables from the dataset
# 'rooms' and 'size' are the features (input variables)
# 'price' is the target variable (what we want to predict)
X = data[['rooms', 'size']]  # Features: rooms and size of the house
y = data['price']  # Target: price of the house (in thousands of dollars)

# Step 4: Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create the Linear Regression model
model = LinearRegression()  # Instantiate a linear regression model

# Step 6: Train the model using the training data
model.fit(X_train, y_train)  # Fit the model to the training data (learn the relationships)

# Step 7: Predict house prices on the test set
y_pred = model.predict(X_test)  # Use the trained model to make predictions on the test data

# Step 8: Evaluate the model's performance
# Calculate Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) to assess model accuracy
mse = mean_squared_error(y_test, y_pred)  # Compute the MSE between the predicted and actual values
rmse = np.sqrt(mse)  # Calculate RMSE, which is a more interpretable error metric
r2 = r2_score(y_test, y_pred)  # Calculate R-squared, which tells how well the model explains the variance

# Print the performance metrics
print(f"Mean Squared Error: {mse:.2f}")  # Print MSE
print(f"Root Mean Squared Error: {rmse:.2f}")  # Print RMSE
print(f"R-squared: {r2:.2f}")  # Print R-squared value

# Step 9: Visualize the data and the regression line
# Create a scatter plot for the original data and plot the regression line
plt.scatter(X['size'], y, color='blue', label='Actual data')  # Scatter plot of the original data
plt.plot(X['size'], model.predict(X), color='red', label='Regression line')  # Plot the regression line
plt.xlabel("Size of House (Square Feet)")  # X-axis label
plt.ylabel("Price (Thousands of Dollars)")  # Y-axis label
plt.title("House Price Prediction")  # Plot title
plt.legend()  # Add a legend to differentiate between data points and regression line
plt.show()  # Display the plot

# Step 10: Predict the price for a new house (example)
# New data point: a house with 6 rooms and 2200 square feet
new_house = np.array([[6, 2200]])  # Input features for the new house (6 rooms, 2200 sq ft)
predicted_price = model.predict(new_house)  # Predict the price of the new house using the model
print(f"Predicted price for a 6-room, 2200 sq ft house: ${predicted_price[0]:.2f}K")  # Print predicted price
