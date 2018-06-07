# coding=utf-8
import requests
import re
import os

header = {'Referer': 'http://www.chsi.com.cn/cet/',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
          'Host': 'www.chsi.com.cn'}


url = "http://www.chsi.com.cn/cet/query"



# 添加参数
def test(num):
    name = "高洪振"
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
        ans = num+name + " " + score[0]

        # 打印该字符串
        print(ans)
        f=open("grade.txt",'a')
        f.write(ans)
        f.close()
        exit(0)
    except:

        # 打印未能成功爬取的人
        print("Error:", num, " ", name)

for room in range(0,200):
    for desk in range(0,31):
        num=370551172100000+room*100+desk
        test(num)
