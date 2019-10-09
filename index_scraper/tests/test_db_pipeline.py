import json
import os
from unittest.mock import Mock

from django.conf import settings
from django.test import TransactionTestCase

from index_scraper.index_scraper.pipelines import IndexScraperPipeline
from index_scraper.index_scraper.spiders.indices import IndicesSpider
from main_board.models import ValueUpdate


class ItemPipelineTest(TransactionTestCase):

    def setUp(self):
        fpath = os.path.join(
            settings.BASE_DIR,
            'index_scraper/tests/values.json'
        )
        with open(fpath, 'r') as f:
            self.items = json.load(f)

    def test_pipeline_saves_items_to_db(self):
        spider = IndicesSpider(limit=1)
        pipeline = IndexScraperPipeline()

        # Artificially set market in session
        ValueUpdate.is_open = Mock(return_value=True)

        # Run each item through data pipeline
        for item in self.items:
            pipeline.process_item(item, spider)

        # All items should be saved to db
        self.assertEqual(
            len(self.items),
            ValueUpdate.objects.count()
        )
