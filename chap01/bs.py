# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

__author__ = 'lzhao'
__date__ = '5/1/16'
__time__ = '2:46 PM'

html = urllib2.urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html, "html.parser")
print (bsObj.h1)
