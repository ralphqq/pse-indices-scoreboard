import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from index_scraper.index_scraper.spiders.indices import IndicesSpider


class IndicesCrawler:
    def __init__(self):
        os.environ.setdefault(
            'SCRAPY_SETTINGS_MODULE',
            'index_scraper.index_scraper.config'
        )
        self.process = CrawlerProcess(get_project_settings())
        self.spider = IndicesSpider

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()
