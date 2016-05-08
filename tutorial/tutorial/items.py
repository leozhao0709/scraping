# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class TutorialItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()


def filter_price(value):
	if value.isdigit():
		return value


class Product(scrapy.Item):
	name = scrapy.Field(
		input_processor=MapCompose(remove_tags),
		output_processor=Join()
	)
	price = scrapy.Field(
		input_processor=MapCompose(remove_tags, filter_price),
		output_processor=TakeFirst()
	)
	stock = scrapy.Field()
	last_update = scrapy.Field(serializer=str)


class DiscountedProduct(Product):
	discount_percent = scrapy.Field(serializer=str)
	discount_expiration_date = scrapy.Field()


class SpecificProduct(Product):
	name = scrapy.Field(Product.fields['name'], serializer=str)
