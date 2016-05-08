# -*- coding: utf-8 -*-

import scrapy

from tutorial.items import DmozItem

__author__ = 'lzhao'
__date__ = '5/6/16'
__time__ = '11:49 PM'


class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
		"http://www.dmoz.org/Computers/Programming/Languages/Python/",
	]

	def parse(self, response):
		for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		for selector in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = selector.xpath('a/text()').extract()
			item['link'] = selector.xpath('a/@href').extract()
			item['desc'] = selector.xpath('text()').extract()
			yield item
