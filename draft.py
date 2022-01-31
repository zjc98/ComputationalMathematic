import numpy as np


def fx(a, b):
    # ans = (x2 * x1 ** 2 + x2 ** 2 * x1 + 1) / (x2 ** 2 + x1 ** 2 + x1 * x2 - 3)

    return ans

# ans = fx(1.8810939357907253,1.9)
# print(ans)

a = np.array([[2,1,-3,-1],[3,1,0,7],[-1,2,4,-2],[1,0,-1,5]])
b = np.linalg.inv(a)
# print(b)
print(np.linalg.det(np.array([[1,2,6],[2,5,15],[6,15,46]])))