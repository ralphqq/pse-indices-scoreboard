# -*- coding: utf-8 -*-

import scrapy


class IndexScraperItem(scrapy.Item):
    name = scrapy.Field()
    current_value = scrapy.Field()
    points_change = scrapy.Field()
    percent_change = scrapy.Field()
    market_status = scrapy.Field()
