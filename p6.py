import sys

codes = {
6: r'''
import math

# Function: f(x) = x^2
# Gradient: f'(x) = 2x

x = 10.0
learning_rate = 1.0
epsilon = 1e-8
G = 0.0

print("AdaGrad Optimization")
print("--------------------")

for i in range(10):
    # Calculate gradient
    gradient = 2 * x

    # Accumulate squared gradient
    G = G + gradient ** 2

    # Update x
    x = x - (learning_rate / (math.sqrt(G) + epsilon)) * gradient

    print("Iteration", i + 1,
          ": x =", round(x, 4),
          "f(x) =", round(x ** 2, 4))

print("\nFinal x =", round(x, 4))
print("Minimum value =", round(x ** 2, 4))
''',
}

n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
print(codes.get(n, "Available practicals: " + str(list(codes))))
