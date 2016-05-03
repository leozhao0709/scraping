# -*- coding: utf-8 -*-
import re
from urllib2 import urlopen
import random
import datetime

from bs4 import BeautifulSoup

__author__ = 'lzhao'
__date__ = '5/2/16'
__time__ = '10:27 PM'

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print link.attrs['href']
# 	# print link.attrs

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")}):
# 	if 'href' in link.attrs:
# 		print link.attrs['href']
# 	# print link.attrs

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	return bsObj.find("div", {"id": "bodyContent"}).findAll("a", {"href": re.compile("^(/wiki/)((?!:).)*$")})

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)


