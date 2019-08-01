# -*- coding: utf-8 -*-
import scrapy


class IndicesSpider(scrapy.Spider):
    name = 'indices'
    allowed_domains = ['www.pse.com.ph/stockMarket/home.html']
    start_urls = ['http://www.pse.com.ph/stockMarket/home.html/']

    def parse(self, response):
        pass
