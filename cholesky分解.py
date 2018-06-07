# 利用乔列斯基法解方程组
import numpy as np

A = np.array([[5, 2, 1, 0],
              [2, 6, -2, -2],
              [1, -2, 5.5, 2],
              [0, -2, 2, 5.5]
              ], dtype=float)
b = np.array([2, 2, -4, 0], dtype=float)


def cholesky(A):
    n = len(A)

    L = []
    for i in range(n):
        L.append([0.0] * n)

    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if i == k:
                L[i][k] = np.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L


if __name__ == '__main__':
    # A=L*L.T
    l = np.array(cholesky(A))
    print("L:\n", l)
    # Ly=b
    y = np.linalg.solve(l, b)
    print("y:\n",y)
    # L.T*x=y
    x = np.linalg.solve(l.T, y)
    print("x:\n",x)
