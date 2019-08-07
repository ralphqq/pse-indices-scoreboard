from __future__ import absolute_import, unicode_literals

from celery import task

from index_scraper.crawl import run_crawler


@task(name='index_getter')
def get_current_index_values():
    run_crawler()
