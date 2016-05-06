# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

__author__ = 'lzhao'
__date__ = '5/1/16'
__time__ = '5:15 PM'

html = urllib2.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
	print name.get_text()

allText = bsObj.findAll(id="text")
print allText[0].get_text()
