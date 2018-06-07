# coding=utf-8
import requests
import re
import os
# 自定义头文件
header = {'Referer': 'http://www.chsi.com.cn/cet/',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
          'Host': 'www.chsi.com.cn'}

# 学信网的url
url = "http://www.chsi.com.cn/cet/query"


# # name.txt是含有姓名和准号证号（15位）的txt，排列规则为每一行：准考证号 姓名，例如：500000000000000 张三
# data_in = open("name.txt", "r+", encoding='utf-8')
# text = data_in.readlines()
#
# # 读取每一行的准考证号和姓名
# for line in text:
#
#     # 去掉末尾空格
#     line = line.strip('\n')
#
#     # 准考证号为15位
#     num = line[0:15]
#
#     # 如果名字是2个字，取这两个字，如果大于等于三个字，取前三个字（学信网姓名一栏仅让输入3个字）
#     if len(line) < 18:
#         name = line[16:18]
#     else:
#         name = line[16:19]

# 添加参数
def test(num):
    name = "石长江"
    param = {
        'zkzh': num,
        'xm': name
    }

    # 构造get
    responce = requests.get(url, headers=header, params=param)

    # 为了方便正则表达式找总分，去掉所有换行符
    newtext = responce.text.replace('\n', '')

    try:
        # 正则表达式找到总分
        score = re.findall('<span class="colorRed">.*?(\d+)', newtext)

        # 输出“姓名+总分”字符串
        ans = name + " " + score[0]

        # 打印该字符串
        print(ans)
        os.system("pause");
    except:

        # 打印未能成功爬取的人
        print("Error:", num, " ", name)

# for room in range(0,200):
for desk in range(0,31):
    num=370551172114800+desk
    test(num)
