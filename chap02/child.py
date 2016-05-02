# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

__author__ = 'lzhao'
__date__ = '5/1/16'
__time__ = '5:51 PM'

html = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# for i in bsObj.div.findAll("img"):
# 	print "##########", i, len(bsObj.div.findAll("img")), "#####"

# for child in bsObj.find("table", {"id": "giftList"}).children:
# 	print child

# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
# 	print sibling

# for sibling in bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_siblings:
# 	print sibling

print bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
