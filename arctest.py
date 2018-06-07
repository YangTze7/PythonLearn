from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.tesla.com/findus/list/superchargers/United+States'
html = request.urlopen(url)

soup = BeautifulSoup(html.read(), "html.parser")
print(soup.body.text.encode('utf-8', 'ignore').decode('utf-8'))
with open("D:/B.txt", 'a', encoding='utf-8') as f:
    f.write(soup.body.text.encode('utf-8', 'ignore').decode('utf-8') + '\n')