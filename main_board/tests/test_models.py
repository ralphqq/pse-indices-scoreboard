import json
import os

from django.conf import settings
from django.test import TestCase

from main_board.models import MarketIndex


class MarketIndexModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with open(os.path.join(settings.BASE_DIR, 'tickers.json'), 'r') as fp:
            cls.expected_records = json.load(fp)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_db_has_correct_number_of_indices(self):
        self.assertEqual(
            len(self.expected_records),
            MarketIndex.objects.count()
        )

    def test_all_indices_in_db_are_valid(self):
        valid_tickers = [item['ticker'] for item in self.expected_records]
        for ind in MarketIndex.objects.all():
            self.assertIn(ind.ticker, valid_tickers)
