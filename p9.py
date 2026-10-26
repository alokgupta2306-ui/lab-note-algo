import sys

codes = {
9: r'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel

# Objective function
def objective_function(x):
    return x**2 + np.sin(x)

# Training data
X = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4]).reshape(-1, 1)

# Function values
y = objective_function(X.ravel())

# Create Gaussian Process kernel
kernel = ConstantKernel(1.0) * RBF(length_scale=1.0)

# Create Gaussian Process model
model = GaussianProcessRegressor(
    kernel=kernel,
    random_state=42
)

# Train the model
model.fit(X, y)

# Test points
X_test = np.linspace(-5, 5, 100).reshape(-1, 1)

# Prediction
y_pred, y_std = model.predict(X_test, return_std=True)

# Display predictions
print("Gaussian Process Surrogate Model")
print("--------------------------------")

test_values = [-3.5, -1.5, 0.5, 1.5, 3.5]

for x in test_values:
    prediction, uncertainty = model.predict(
        [[x]],
        return_std=True
    )
    print("x =", x)
    print("Predicted Value =", prediction[0])
    print("Uncertainty =", uncertainty[0])
    print()

# Plot actual function
plt.plot(
    X_test,
    objective_function(X_test.ravel()),
    label="Actual Function"
)

# Plot GP prediction
plt.plot(
    X_test,
    y_pred,
    label="GP Prediction"
)

# Plot uncertainty
plt.fill_between(
    X_test.ravel(),
    y_pred - 2 * y_std,
    y_pred + 2 * y_std,

    alpha=0.2,
    label="95% Confidence Interval"
)

# Training points
plt.scatter(
    X,
    y,
    label="Training Data"
)

plt.xlabel("X")
plt.ylabel("Function Value")
plt.title("Gaussian Process Surrogate Model")
plt.legend()
plt.show()
''',
}

n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
print(codes.get(n, "Available practicals: " + str(list(codes))))
