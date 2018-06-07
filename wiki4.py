import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages=set()
def get_links(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org/"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id = "mw-content-text").find_all("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面少了一些属性")
    for link in bsObj.find_all("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新页面
                newPage=link.attrs['href']
                print("-----------------------\n"+newPage)
                pages.add(newPage)
                get_links(newPage)
get_links("")


