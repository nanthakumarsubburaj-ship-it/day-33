# Simple Linear Regression using scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (2D array)
y = np.array([10, 20, 30, 40, 50])            # Dependent variable

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict a new value
predicted_value = model.predict([[6]])
print("Predicted Value for 6:", predicted_value[0])
