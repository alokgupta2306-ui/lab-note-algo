import sys

codes = {
7: r'''
import numpy as np
import matplotlib.pyplot as plt

# Training data
X = np.array([0, 1, 2, 3, 4, 5])
y = np.sin(X)

# Gaussian Radial Basis Function
def rbf(x, center, epsilon=1.0):
    return np.exp(-((x - center) / epsilon) ** 2)

# Create RBF matrix
Phi = np.zeros((len(X), len(X)))
for i in range(len(X)):
    for j in range(len(X)):
        Phi[i, j] = rbf(X[i], X[j])

# Calculate weights
weights = np.linalg.solve(Phi, y)

# Prediction function
def predict(x):
    result = 0
    for i in range(len(X)):
        result += weights[i] * rbf(x, X[i])
    return result

# Test points
X_test = np.linspace(0, 5, 100)
y_pred = np.array([predict(x) for x in X_test])

# Display some predictions
print("RBF Surrogate Model")
print("-------------------")

for x in [0.5, 1.5, 2.5, 3.5, 4.5]:
    print("x =", x, "Predicted =", predict(x))

# Plot
plt.scatter(X, y, label="Actual Data")
plt.plot(X_test, y_pred, label="RBF Surrogate")
plt.xlabel("X")
plt.ylabel("Function Value")
plt.title("Radial Basis Function Surrogate Model")
plt.legend()
plt.show()
''',
}

n = int(sys.argv[1]) if len(sys.argv) > 1 else 7
print(codes.get(n, "Available practicals: " + str(list(codes))))
