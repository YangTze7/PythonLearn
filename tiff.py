import gdal
import numpy as np
import os
from math import sqrt


def file_name(file_dir):
    l = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.tif':
                l.append(os.path.join(root, file))
    return l


def read_tif(file_name):
    dataset = gdal.Open(file_name)
    if dataset == None:
        print(file_name + "文件无法打开")
        return
    im_width = dataset.RasterXSize  # 栅格矩阵的列数
    im_height = dataset.RasterYSize  # 栅格矩阵的行数
    im_bands = dataset.RasterCount  # 波段数
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)  # 获取数据
    return im_data
    # im_geotrans = dataset.GetGeoTransform()#获取仿射矩阵信息
    # im_proj = dataset.GetProjection()#获取投影信息
    # im_blueBand =  im_data[0,0:im_height,0:im_width]#获取蓝波段
    # im_greenBand = im_data[1,0:im_height,0:im_width]#获取绿波段
    # im_redBand =   im_data[2,0:im_height,0:im_width]#获取红波段
    # im_nirBand = im_data[3,0:im_height,0:im_width]#获取近红外波段

def multipl(a, b):
    sumofab = 0.0
    for i in range(len(a)):
        temp = a[i] * b[i]
        sumofab += temp
    return sumofab


def corrcoef(x, y):
    n = len(x)
    # 求和
    sum1 = np.sum(x)
    sum2 = np.sum(y)
    # 求乘积之和
    sumofxy = multipl(x, y)
    # 求平方和
    sumofx2 = np.sum([pow(i, 2) for i in x])
    sumofy2 = np.sum([pow(j, 2) for j in y])
    num = sumofxy - (float(sum1) * float(sum2) / n)
    # 计算皮尔逊相关系数
    den = sqrt((sumofx2 - float(sum1 ** 2) / n) * (sumofy2 - float(sum2 ** 2) / n))
    return num / den


def band_corr(band1: object, band2: object) -> object:
    band1 = np.array(band1)
    band2 = np.array(band2)
    band1 = band1.flatten()
    band2 = band2.flatten()
    band_corr1 = np.corrcoef(band1, band2)
    return band_corr1


print("请输入图像文件夹")
# p = input()
p = "D:\\ETM"
path = file_name(p)


b = []

# b1 = read_tif("b1.tif")
# b2 = read_tif("b2.tif")
# b3 = read_tif("b3.tif")
# b4 = read_tif("b4.tif")
# b5 = read_tif("b5.tif")
# b = [b1, b2, b3, b4, b5]


size = len(path)

for i in range(size):
    b.append(read_tif(path[i]))

# input()
y = np.zeros((size, size))
x = y.tolist()
file = open('data.txt', 'w')
for i in range(size):
    for j in range(size):
        x[i][j] = band_corr(b[i], b[j])[0, 1]
        print("%.3f" % x[i][j], end=' ')
        if j == (size - 1):
            print('\n')
file.write(str(x))
file.close()



