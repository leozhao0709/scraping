# -*- coding: utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

__author__ = 'lzhao'
__date__ = '5/4/16'
__time__ = '10:43 PM'

pages = set()


def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print newPage
				pages.add(newPage)
				getLinks(newPage)


getLinks("")
