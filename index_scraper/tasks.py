from celery import task

from index_scraper.crawl import IndicesCrawler


@task(name='index_getter')
def get_current_index_values(**kwargs):
    crawler = IndicesCrawler(**kwargs)
    crawler.run_spider()
