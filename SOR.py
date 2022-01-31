import numpy as np

data_A = np.loadtxt('A.txt')
data_b = np.loadtxt('b.txt')
data_x = np.loadtxt('x.txt')
# print(data_A@data_x-data_b)
approximate_solution = np.linalg.solve(data_A, data_b)

w = 1.1
x = np.zeros_like(data_b)
x_new = np.zeros_like(data_b)

iteration = 0
# for it in range(200):
while True:
    iteration = iteration + 1
    for i in range(x.shape[0]):
        x[i] = x[i] + w / data_A[i, i] * (data_b[i] - data_A[i].T @ x)
    max_err = np.linalg.norm(approximate_solution - x, ord=np.inf)
    # print(f'The {iteration} : max error:{max_err}')
    if max_err < (10 ** -6):
        break

print(f'The {iteration} : max error:{max_err}')  # The 11145 : max error:9.998555455803526e-07
np.savetxt('SOR Result.txt', x)