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

        # Customize crawl settings
        s = get_project_settings()
        s['SPIDER_MODULES'] = ['index_scraper.index_scraper.spiders']
        s['NEWSPIDER_MODULE'] = 'index_scraper.index_scraper.spiders'
        s['ITEM_PIPELINES'] = {
            'index_scraper.index_scraper.pipelines.IndexScraperPipeline': 300,
        }

        self.process = CrawlerProcess(s)
        self.spider = IndicesSpider

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()
