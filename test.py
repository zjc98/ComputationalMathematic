import numpy as np

A = np.loadtxt('A.txt')
b = np.loadtxt('b.txt')
x = np.loadtxt('x.txt')

x_result = np.dot(b, np.linalg.inv(A))
print(max(x_result - x))