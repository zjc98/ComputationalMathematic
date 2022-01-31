import numpy as np

arr = np.array([[0.4096, 0.1234, 0.3678, 0.2943], [0.2246, 0.3872, 0.4015, 0.1129], [0.3645, 0.1920, 0.3781, 0.0643],
                [0.1784, 0.4002, 0.2786, 0.3927]])
x = np.array([0.4043, 0.1550, 0.4240, -0.2557]).reshape((4, 1))
arr_inv = np.linalg.inv(arr)
# print(f"精确解：\n{np.dot(arr_inv, x)}")

arr_2 = np.c_[arr, x]


def gauss(matrix):
    h = matrix.shape[0]
    for i in range(h - 1):
        for k in range(i + 1, h):
            for j in range(i + 1, h + 1):
                # print(matrix[i + 1, j],matrix[i, j] , matrix[i + 1, j], matrix[i, i])
                matrix[k, j] = matrix[k, j] - matrix[i, j] * (matrix[k, i] / matrix[i, i])
                # matrix = np.around(matrix, 4)
        matrix[i + 1:h, i] = 0
        print(f'高斯消去第{i}轮:\n{matrix}')
    return matrix


def gauss_col(matrix):
    h = matrix.shape[0]
    for i in range(h - 1):
        max_index = np.argmax(np.abs(matrix[i:, i]))
        max_index = max_index + i
        if max_index != i:
            matrix[[i, max_index], :] = matrix[[max_index, i], :]
        for k in range(i + 1, h):
            for j in range(i + 1, h + 1):
                # print(matrix[i + 1, j],matrix[i, j] , matrix[i + 1, j], matrix[i, i])
                matrix[k, j] = matrix[k, j] - matrix[i, j] * (matrix[k, i] / matrix[i, i])
                matrix = np.around(matrix, 4)
        matrix[i + 1:h, i] = 0

        print(f'高斯消去列主元第{i}轮:\n{matrix}')
    matrix = np.around(matrix, 4)
    return matrix


def calcu(answer):
    # x4 = answer[3, 4] / answer[3, 3]
    x3 = (answer[2, 3]) / answer[2, 2]
    x2 = (answer[1, 3] - answer[1, 2] * x3) / answer[1, 1]
    x1 = (answer[0, 3] - answer[0, 2] * x3 - answer[0, 1] * x2) / answer[0, 0]
    print(f"消去解:\n{x1, x2, x3}")


# calcu(gauss(arr_2))
# calcu(gauss_col(arr_2))

# assignment 2
arr_3 = np.array(
    [[0.6428, 0.3475, -0.8468, 0.4127], [0.3475, 1.8423, 0.4759, 1.7321], [-0.8468, 0.4759, 1.2147, -0.8621]])
x = arr_3[:, -1].reshape((3, 1))
arr_inv = np.linalg.inv(arr_3[:,:-1])
print(f"精确解：\n{np.dot(arr_inv, x)}")
print(gauss(arr_3))
calcu(gauss(arr_3))