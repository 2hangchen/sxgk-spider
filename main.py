# -*- coding: utf-8 -*
from lxml import etree
import xml.etree.ElementTree as ET
import urllib
import time
import datetime
import xlwt
from asq.initiators import query

def getHtml(url):
    html = urllib.urlopen(url).read()
    return html
data = list()
urls = ['http://www.sxkszx.cn/news/201888/n649238402.html']
for url in urls:
    html = getHtml(url)
    tree =etree.HTML(html)
    rows =tree.xpath('//div[@id="newsbody_class"]//tr')
    #print rows
    for row in rows:
        #print etree.tostring(row)
        #strs=(etree.tostring(row,encoding = "UTF-8").decode('utf-8'))
        strs = (etree.tostring(row.xpath('//td/span'), encoding="UTF-8").decode('utf-8'))
        print strs
        #data.append([strs,row.getchildren()[1].text.replace('\t','').replace('\r\n',''),row.getchildren()[2].text.replace('\t','').replace('\r\n',''),row.getchildren()[3].text.replace('\t','').replace('\r\n','')])
    time.sleep(1)
for row in data: print(row)
print(len(data))
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet('demo')
index = 0
for row in data:
    for x, item in enumerate(row):
        data_sheet.write(index, x, item)
    index += 1
workbook.save('demo.xls')
