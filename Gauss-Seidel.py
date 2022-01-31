import numpy as np

data_A = np.loadtxt('A.txt')
data_b = np.loadtxt('b.txt')
data_x = np.loadtxt('x.txt')
# print(data_A@data_x-data_b)
approximate_solution = np.linalg.solve(data_A, data_b)

x = np.zeros_like(data_b)
x_new = np.zeros_like(data_b)

iteration = 0
# for it in range(2000):
while True:
    iteration = iteration + 1
    for i in range(x.shape[0]):
        if i == 0:
            x[i] = 1 / data_A[i, i] * (data_b[i] - data_A[i, 1:].T @ x[1:])
        else:
            A_item = np.delete(data_A[i], i)
            x_item = np.delete(x, i)
            x[i] = 1 / data_A[i, i] * (data_b[i] - A_item.T @ x_item)

    max_err = np.linalg.norm(approximate_solution - x, ord=np.inf)
    # print(f'The {iteration} : max error:{max_err}')
    if max_err < (10 ** -6):
        break
print(f'The {iteration} : max error:{max_err}')    # The 13624 : max error:9.990490141831287e-07
np.savetxt('Gauss-Serdel Result.txt', x)
# print(max(data_A @ approximate_solution - data_b))
