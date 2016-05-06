# -*- coding: utf-8 -*-

from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

__author__ = 'lzhao'
__date__ = '5/1/16'
__time__ = '3:01 PM'


def get_title(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html, "html.parser")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title


title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title is None:
	print "Title could not be found"
else:
	print title
