import numpy as np

n = 10
x = np.linspace(0, 1, n + 1)
y = np.zeros_like(x)
y[0] = 1
# trapezoid
for i in range(1, len(x)):
    y[i] = (1 - np.exp(-x[i])) / x[i]
    # y[i] = x[i] / (4 + x[i] ** 2)

h = 1 / n
# trapezoid = h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
# print(trapezoid)

# simpson
x2 = np.zeros(n)
y2 = np.zeros(n)
for j in range(n):
    x2[j] = (x[j] + x[j + 1]) / 2
    y2[j] = (1 - np.exp(-x2[j])) / x2[j]

simpson = h / 6 * (y[0] + 4 * np.sum(y2) + 2 * np.sum(y[1:-1]) + y[-1])
print(simpson)
