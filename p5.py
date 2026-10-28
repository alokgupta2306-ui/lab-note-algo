import numpy as np
from scipy.optimize import minimize

def f(x):
    return -(x[0] - 3)**2 + 9

def objective(x):
    return -f(x)

x0 = [0]

result = minimize(objective, x0, method='BFGS')

print("Quasi-Newton Method (BFGS)")
print("--------------------------------")
print("Optimal x =", round(result.x[0], 4))
print("Maximum value =", round(f(result.x), 4))
print("Number of iterations =", result.nit)
print("Success =", result.success)
