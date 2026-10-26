import sys

codes = {
3: '''
import numpy as np

def f(x):
    return (x - 2) ** 2

def quadratic_fit_search(x1, x2, x3, tolerance=1e-6, max_iter=100):
    pts = [x1, x2, x3]
    x_old = None
    for i in range(max_iter):
        a, b, c = pts
        fa, fb, fc = f(a), f(b), f(c)
        # Minimum of the parabola through the three points
        num = (b**2 - c**2) * fa + (c**2 - a**2) * fb + (a**2 - b**2) * fc
        den = 2 * ((b - c) * fa + (c - a) * fb + (a - b) * fc)
        if den == 0:
            break
        x_new = num / den
        if x_old is not None and abs(x_new - x_old) < tolerance:
            break
        x_old = x_new
        # Add the new point and drop the worst one
        pts.append(x_new)
        pts.remove(max(pts, key=f))
    minimum = min(pts, key=f)
    print("Minimum point =", minimum)
    print("Minimum value =", f(minimum))

# Call the function
quadratic_fit_search(0, 1, 5)
''',
}

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
print(codes.get(n, "Available practicals: " + str(list(codes))))
