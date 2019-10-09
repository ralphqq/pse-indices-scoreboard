from unittest.mock import patch

from django.test import TestCase

from index_scraper.crawl import IndicesCrawler
from index_scraper.tasks import get_current_index_values


class CrawlProcessTest(TestCase):

    @patch(
        'index_scraper.index_scraper.spiders'
        '.indices.IndicesSpider.start_requests'
    )
    def test_crawl_process_starts_request(self, mock_request):
        crawler = IndicesCrawler()
        crawler.run_spider()
        self.assertEqual(mock_request.called, True)

    @patch('index_scraper.crawl.CrawlerProcess.crawl')
    def test_celery_task_launches_crawl_process(self, mock_crawl):
        get_current_index_values()
        self.assertEqual(mock_crawl.called, True)
