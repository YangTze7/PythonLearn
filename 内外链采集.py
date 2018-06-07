from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import re
import random

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks=[]
    #找出所有以"/"开头的链接
    for link in bsObj.find_all("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not  None:
            if(link.attrs['href'].startswith('/')):
                internalLinks.append(includeUrl+link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    excludeUrlLinks = []
    #找出所有以"http"或者"www"开头但不包括当前url的链接
    for link in bsObj.find_all("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs not in excludeUrlLinks:
                excludeUrlLinks.append(link.attrs['href'])
    return excludeUrlLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No exterl links")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj,domain)
        return getRandomExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])

    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print("Random external link is:"+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://www.ixxin.cn/")



