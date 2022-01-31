import numpy as np

def newton(x):
    # fx = x - (x ** 3 - 3 * x - 1) / (3 * x ** 2 - 3)
    fx = x - (x - np.tan(x)) / (1 - 1 / (np.cos(x) ** 2))
    return fx

x = 4.5
for i in range(6):
    x = newton(x)
    print(x)