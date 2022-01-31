import numpy as np


def power_method(A, iters, print_=True):
    A_size = np.shape(A)[0]
    v = np.ones((A_size, 1))
    v = np.dot(A, v)
    u = v / np.max(v)
    if print_:
        print(f'The 1: u:{u.T}, lamda:{max(v)}')
    for iter in range(iters):
        v = np.dot(A, u)
        u = v / np.max(v)
        if print_:
            print(f'The {iter + 2}: u:{u.T}, lamda:{max(v)}')


# A = np.array([[1, 1, 0.5], [1, 1, 0.25], [0.5, 0.25, 2]])
A = np.array([[3, -4, 3], [-4, 6, 3], [3, 3, 1]])
power_method(A, 20)

