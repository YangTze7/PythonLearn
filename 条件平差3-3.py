# 三角高程平差计算
import numpy as np
# 初始条件
Ha = 5.016
Hb = 6.016
L = np.matrix([1.359, 2.009, 0.363, 1.012, 0.657, -0.357], dtype=float).T
# 条件方程组
A = np.matrix([[1, -1, 0, 0, 1, 0],
               [0, 0, 1, -1, 1, 0],
               [0, 0, 1, 0, 0, 1],
               [0, 1, 0, -1, 0, 0]], dtype=float)
A0=np.matrix([0,0,0,Ha-Hb]).T
# 由边长定权
lengths = np.diag((1.05, 1.30, 1.52, 1.64, 1.55, 2.00))
Q = np.matrix((lengths * lengths))


def condition_adjust(L, A, A0, Q):
    #闭合差
    W = -(A*L+A0)
    # 法方程系数
    N = A * Q * A.T
    # 乘常数
    K = N ** -1 * W
    # 改正数
    V = Q * A.T * K
    # 输出改正数
    print("改正数：\n",V)
    # 平差值
    L = L + V
    # 输出平差值
    print("平差值：\n", L)
    # 返回平差值
    return L

if __name__ == '__main__':
    result = condition_adjust(L, A, A0, Q)
