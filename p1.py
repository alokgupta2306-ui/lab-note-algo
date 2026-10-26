import sys

codes = {
1: '''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
plt.contour(X, Y, Z)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot of Z = X^2 + Y^2")
plt.show()
''',
# 2: ''' next practical ''',
}

n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
print(codes.get(n, "Available practicals: " + str(list(codes))))
