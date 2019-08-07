from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from index_scraper.spiders.indices import IndicesSpider


def run_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(IndicesSpider)
    process.start()

if __name__ == '__main__':
    run_crawler()
