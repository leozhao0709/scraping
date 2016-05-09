# -*- coding: utf-8 -*-
import socket
import datetime
import scrapy
import urlparse
import json
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.http import Request


class BasicSpider(scrapy.Spider):
	name = "api"
	allowed_domains = ["localhost"]
	start_urls = (
		'http://localhost:9312/properties/api.json',
	)

	def parse(self, response):
		base_url = "http://localhost:9312/properties/"
		js = json.loads(response.body)
		for item in js:
			id = item["id"]
			url = base_url + "property_%06d.html" % id
			yield Request(url, callback=self.parse_item)

	def parse_item(self, response):
		"""
		This function parses a property page.

		@url http://localhost:9312/properties/property_000000.html
		@returns items 1
		@scrapes title price description address image_urls
		@scrapes url project spider server date
		"""
		l = ItemLoader(item=PropertiesItem(), response=response)
		l.add_xpath('title', '//*[@itemprop="name"][1]/text()', MapCompose(unicode.strip, unicode.title))
		l.add_xpath('price', '//*[@itemprop="price"][1]/text()', MapCompose(lambda i: i.replace(',', ''), float),
					re='[,.0-9]+')
		l.add_xpath('description', '//*[@itemprop="description"][1]/text()', MapCompose(unicode.strip), Join())
		l.add_xpath('address', '//*[@itemtype="http://schema.org/Place"][1]/text()', MapCompose(unicode.strip))
		l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
					MapCompose(lambda i: urlparse.urljoin(response.url, i)))

		# Housekeeping fields
		l.add_value('url', response.url)
		l.add_value('project', self.settings.get('BOT_NAME'))
		l.add_value('spider', self.name)
		l.add_value('server', socket.gethostname())
		l.add_value('date', datetime.datetime.now())
		return l.load_item()
