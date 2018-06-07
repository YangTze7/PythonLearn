import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages=set()
def get_links(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org/"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find_all("a",href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)

get_links(" ")    
