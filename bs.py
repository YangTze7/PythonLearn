from urllib.request import urlopen
from bs4 import BeautifulSoup

# html=urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj=BeautifulSoup(html.read())
# print(bsObj.h1)


# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
# nameList = bsObj.find_all("span", {"class": "green"})
# for name in nameList:
#     print(name.get_text())

html=urlopen('http://www.pythonscaping.com/pages/page3.html');
bsObj=BeautifulSoup(html)
print(bsObj.find_all("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
