# -*- coding: utf-8 -*-  
import os, sys
import urllib
from bs4 import BeautifulSoup

# 体彩 排列5  
URL = "http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw"
page = urllib.urlopen(URL)
soup = BeautifulSoup(page)
page.close()

fp = open("pl5.txt", "w")
tables = soup.findAll('table')
tab = tables[0]
for tr in tab.tbody.findAll('tr'):
    for td in tr.findAll('td'):
        text = td.getText().encode('cp936') + '!'
        fp.write(text)
    fp.write('\n')
#  
fp.close()  