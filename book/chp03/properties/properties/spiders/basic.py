# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["localhost"]
    start_urls = (
        'http://www.localhost/',
    )

    def parse(self, response):
        pass
