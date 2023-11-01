import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1, 1], [5, 3], [6, 4], [10, 4], [11, 2]])
y = np.array([0, 2, 2, 6, 9])

# Train
reg = LinearRegression().fit(x, y)

# Test
y_pred = reg.predict(np.array([[7, 2], [12, 5], [100, 22], [100, 23]]))
print(f"Predicted data: {y_pred}")

# Error
y_actual = np.array([5, 7, 78, 77])
print(f"Actual data: {y_actual}")
error = y_pred - y_actual
print(f"Error: {error}")