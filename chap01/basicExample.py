# -*- coding: utf-8 -*-

import urllib2

__author__ = 'lzhao'
__date__ = '5/1/16'
__time__ = '2:38 PM'

html = urllib2.urlopen("http://pythonscraping.com/pages/page1.html")
print html.read()
