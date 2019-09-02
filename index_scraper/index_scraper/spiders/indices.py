# -*- coding: utf-8 -*-
from datetime import datetime
import json
import logging

import pytz
import scrapy

from ..items import IndexScraperItem


class IndicesSpider(scrapy.Spider):
    name = 'indices'
    allowed_domains = ['www.pse.com.ph']
    start_urls = ['http://www.pse.com.ph/stockMarket/home.html']
    headers = {
        'Host': 'www.pse.com.ph',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.pse.com.ph/stockMarket/home.html',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    def __init__(self, db_mode='save', *args, **kwargs):
        """Overrides spider constructor to accept custom argument.

        Params:
            db_mode (str): flag to indicate whether or not to save to db; 
                value can either be:
                    'skip': does not save scraped items to db
                    'save': saves items only during market session
                    'force': saves items even when market is closed
        """
        if db_mode.lower() not in ['save', 'force', 'skip']:
            raise ValueError("db_mode accepts 'skip', 'force' or 'save'.")
        self.db_mode = db_mode.lower()
        super().__init__(*args, **kwargs)

    def parse(self, response):
        yield scrapy.Request(
            url=self.get_url(),
            method='GET',
            headers=self.headers,
            callback=self.parse_object
        )

    def parse_object(self, response):
        records = json.loads(response.text).get('records')
        if records:
            for record in records:
                item = IndexScraperItem()
                item['name'] = record['indexName']
                item['current_value'] = record['indexPoints']
                item['points_change'] = record['changeValue']
                item['percent_change'] = record['percentageChange']
                item['market_status'] = record['marketStatus']

                yield item

        else:
            logging.log(logging.INFO, 'No data obtained')

    def get_url(self):
        utc_now = pytz.utc.localize(datetime.utcnow())
        phl_now = utc_now.astimezone(pytz.timezone('Asia/Manila'))
        ts = int(phl_now.timestamp()) * 1000
        return f'https://www.pse.com.ph/stockMarket/dailySummary.html?method=getMarketIndices&ajax=true&_dc={ts}'

