import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

def objective_function(x):
    return x**2 + np.sin(x)

X = np.linspace(-5, 5, 30).reshape(-1, 1)

y = objective_function(X.ravel())

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

X_test = np.linspace(-5, 5, 200).reshape(-1, 1)

y_pred = model.predict(X_test)

print("Random Forest Surrogate Model")
print("-----------------------------")

test_values = [-4, -2, 0, 2, 4]

for x in test_values:
    prediction = model.predict([[x]])[0]
    actual = objective_function(x)

    print("x =", x)
    print("Actual Value =", actual)
    print("Predicted Value =", prediction)
    print()

plt.scatter(X, y, label="Sample Data")
plt.plot(X_test, objective_function(X_test.ravel()),
         label="Actual Function")
plt.plot(X_test, y_pred,
         label="Random Forest Surrogate")
plt.xlabel("X")
plt.ylabel("Function Value")
plt.title("Random Forest Surrogate Model")
plt.legend()
plt.show()
