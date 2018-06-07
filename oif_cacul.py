import gdal
import numpy as np
import os

def read_tif(file_name):
    dataset = gdal.Open(file_name)
    if dataset == None:
        print(file_name + "文件无法打开")
        return
    im_width = dataset.RasterXSize  # 栅格矩阵的列数
    im_height = dataset.RasterYSize  # 栅格矩阵的行数
    # im_bands = dataset.RasterCount  # 波段数
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)  # 获取数据
    return im_data
    # im_geotrans = dataset.GetGeoTransform()#获取仿射矩阵信息
    # im_proj = dataset.GetProjection()#获取投影信息
    # im_blueBand =  im_data[0,0:im_height,0:im_width]#获取蓝波段
    # im_greenBand = im_data[1,0:im_height,0:im_width]#获取绿波段
    # im_redBand =   im_data[2,0:im_height,0:im_width]#获取红波段
    # im_nirBand = im_data[3,0:im_height,0:im_width]#获取近红外波段


def band_corr(band1: object, band2: object) -> object:
    band1 = np.array(band1)
    band2 = np.array(band2)
    band1 = band1.flatten()
    band2 = band2.flatten()
    band_corr1 = np.corrcoef(band1, band2)
    return band_corr1


def band_ofi(band1, band2, band3):
    band1 = np.array(band1)
    band2 = np.array(band2)
    band3 = np.array(band3)
    band1 = band1.flatten()
    band2 = band2.flatten()
    band3 = band3.flatten()
    band1_std = band1.std()
    band2_std = band2.std()
    band3_std = band3.std()
    ofi = sum([band1_std, band2_std, band3_std])/sum([band_corr(band1, band2)[0, 1], band_corr(band1, band3)[0, 1], band_corr(band2, band3)[0, 1]])
    return ofi


print("输入波段1、2、3路径：")
# b1_path = input()
# b2_path = input()
# b3_path = input()
b1 = read_tif("b1.tif")
b2 = read_tif("b2.tif")
b3 = read_tif("b3.tif")
# b1 = read_tif(b1_path)
# b2 = read_tif(b2_path)
# b3 = read_tif(b3_path)

print(band_ofi(b1, b2, b3))
input()
os.system("pause")