# 水准高程平差计算
import numpy as np
# 初始条件
Ha = 31.100
Hb = 34.165
h = np.matrix([1.001, 1.002, 1.064, 0.500, 0.504, 0.060, 0.560, 1.000], dtype=float).T
# 条件方程组
A = np.matrix([[0, 1, 0, -1, -1, 0, 0, 0],
               [0, 1, -1, 0, 0, 1, 0, 0],
               [0, 0, 1, -1, 0, 0, -1, 0],
               [1, 0, 1, 0, 0, 0, 0, 1]], dtype=float)
A0 = np.matrix([0, 0, 0, Ha - Hb], dtype=float).T
# 定权
Q = np.diag((1, 2, 2, 1, 2, 2, 2.5, 2.5))


def condition_adjust(h,A,A0,Q):
    # 闭合差
    W = A * h + A0
    # 法方程系数
    N = A * Q * A.T
    # 乘常数
    K = N ** -1 * W
    # 改正数
    V = Q * A.T * K
    # 输出改正数
    print("改正数：\n",V)
    # 平差值
    h = h + V
    # 输出平差值
    print("平差值：\n",h)
    # 返回平差值
    return h


if __name__ == '__main__':
    result = condition_adjust(h,A,A0,Q)

