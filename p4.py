def f(x):
    return x**2

def gradient(x):
    return 2*x

x = 10

learning_rate = 0.1

iterations = 10

print("Gradient Descent")

for i in range(iterations):
    grad = gradient(x)

    x = x - learning_rate * grad

    print("Iteration", i + 1, ": x =", round(x, 4),
          "f(x) =", round(f(x), 4))

print("\nMinimum value occurs approximately at x =", round(x, 4))
