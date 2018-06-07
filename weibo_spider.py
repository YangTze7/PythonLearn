import re
import string
import sys
import os
import urllib
#import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
 
#reload(sys)
#sys.setdefaultencoding('utf-8')
if(len(sys.argv) >=2):
  user_id = (int)(sys.argv[1])
else:
  user_id = (int)(input(u"input user_id: "))
 
cookie = {"Cookie": "T_WM=d5241830327dbb6bf3454754dbec3ce4; SUB=_2A250-SMUDeRhGeNH7FIV8CrNzDuIHXVUAk1crDV6PUJbkdANLWPskW2Og8I3YD0wm7kshB_1j_dKPTMNIQ..; SUHB=0jBIqXb7CFm2wp; SSOLoginState=1509774148; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174%26uicode%3D20000174%26fid%3Dhotword"}
url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id
 
html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
 
result = "" 
urllist_set = set()
word_count = 1
image_count = 1
 
print ('ready...')
 
for page in range(1,pageNum+1):
 
  #lxml page
  url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page) 
  lxml = requests.get(url, cookies = cookie).content
 
  #
  selector = etree.HTML(lxml)
  content = selector.xpath('//span[@class="ctt"]')
  for each in content:
    text = each.xpath('string(.)')
    if word_count >= 4:
      text = "%d :"%(word_count-3) +text+"\n\n"
    else :
      text = text+"\n\n"
    result = result + text
    word_count += 1
 
  #
  soup = BeautifulSoup(lxml, "lxml")
  urllist = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
  first = 0
  for imgurl in urllist:
    urllist_set.add(requests.get(imgurl['href'], cookies = cookie).url)
    image_count +=1
b = bytes(result, encoding='utf-8')
print("file_name:")
file_name = input()
fo = open(file_name+'.txt', "wb")
fo.write(b)
word_path=os.getcwd()+'/%d'%user_id
print ('finish')

 
#link = ""
#fo2 = open('%user_id', "wb")
#for eachlink in urllist_set:
  #link = link + eachlink +"\n"
#fo2.write(link)
#print u''
 
#if not urllist_set:
  #print u''
#else:
  ##
  #image_path=os.getcwd()+'/weibo_image'
  #if os.path.exists(image_path) is False:
    #os.mkdir(image_path)
  #x=1
  #for imgurl in urllist_set:
    #temp= image_path + '/%s.jpg' % x
    #print u'haha' % x
    #try:
      #urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(),temp)
    #except:
      #print u"fail:%s"%imgurl
    #x+=1
 
#print u'ha%d,ha%s'%(word_count-4,word_path)
#print u'ha%d,ha%s'%(image_count-1,image_path)
