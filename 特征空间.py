import gdal
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
#
# dataset1 = gdal.Open("b1.tif")
# dataset2 = gdal.Open("b2.tif")

dataset1 = gdal.Open("D:\dst\\b1.tif")
dataset2 = gdal.Open("D:\dst\\b2.tif")
im_width1 = dataset1.RasterXSize  # 栅格矩阵的列数
im_height1 = dataset1.RasterYSize  # 栅格矩阵的行数
im_bands1 = dataset1.RasterCount  # 波段数
im_data1 = dataset1.ReadAsArray(0, 0, im_width1, im_height1)  # 获取数据


im_width2 = dataset2.RasterXSize  # 栅格矩阵的列数
im_height2 = dataset2.RasterYSize  # 栅格矩阵的行数
im_bands2 = dataset2.RasterCount  # 波段数
im_data2 = dataset2.ReadAsArray(0, 0, im_width2, im_height2)  # 获取数据
value = np.zeros((256, 256),dtype=float)
band1 = np.array(im_data1)
band2 = np.array(im_data2)
band11 = band1.flatten()
band21 = band2.flatten()
band11.astype(int)
band21.astype(int)

pixel_num = im_width1 * im_height1

for x in range(pixel_num):
    value[band11[x]][band21[x]] = value[band11[x]][band21[x]]+1

# m=0
# for i in range(256):
#     for j in range(256):
#         if m < value[i][j]:
#             m = value[i][j]


# print(m)

img = PIL.Image.fromarray(value)

#可以调用Image库下的函数了，比如show()
img.show()
# input()
# img.save("tz.bmp")
# np.savetxt('tz.txt',value)


