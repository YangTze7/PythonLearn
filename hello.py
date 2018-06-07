
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
# import traceback
import re

url = 'https://www.tesla.com/findus/list/superchargers/United+States'
# def getHTMLText(url):

r = requests.get(url)
r.raise_for_status()
r.encoding = r.apparent_encoding
with open("D:/B.txt", 'a', encoding='utf-8') as f
    f.write(str(r) + '\n')
