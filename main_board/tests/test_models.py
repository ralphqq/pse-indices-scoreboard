import json
import os

from django.conf import settings
from django.test import TestCase

from main_board.models import MarketIndex, ValueUpdate


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


class ValueUpdateModelTest(TestCase):

    def test_if_is_open_method_returns_false_if_db_is_empty(self):
        self.assertEqual(ValueUpdate.objects.count(), 0)
        self.assertEqual(ValueUpdate.is_open(), False)
