Code: 
def f(x):
    return (x - 2) ** 2

def quadratic_fit_search(x1, x2, x3, tolerance):
    while abs(x3 - x1) > tolerance:

        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)

        numerator = (x2 - x1) ** 2 * (f2 - f3) - \
                    (x2 - x3) ** 2 * (f2 - f1)

        denominator = 2 * ((x2 - x1) * (f2 - f3) -
                           (x2 - x3) * (f2 - f1))

        if denominator == 0:
            break

        x_new = x2 - numerator / denominator
        f_new = f(x_new)

        if x_new < x2:
            if f_new < f2:
                x3 = x2
                x2 = x_new
            else:
                x1 = x_new
        else:
            if f_new < f2:
                x1 = x2
                x2 = x_new
            else:
                x3 = x_new

    print("Minimum point =", x2)
    print("Minimum value =", f(x2))

quadratic_fit_search(0, 2.5, 5, 0.001)
