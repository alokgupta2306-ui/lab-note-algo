import numpy as np
from scipy.optimize import minimize

# Function whose maximum is required
def f(x):
    return -(x[0] - 3)**2 + 9

# To find maximum, minimize the negative of the function
def objective(x):
    return -f(x)

# Initial value
x0 = [0]

# Quasi-Newton method: BFGS
result = minimize(objective, x0, method='BFGS')

# Display result
print("Quasi-Newton Method (BFGS)")
print("--------------------------------")
print("Optimal x =", round(result.x[0], 4))
print("Maximum value =", round(f(result.x), 4))
print("Number of iterations =", result.nit)
print("Success =", result.success)
