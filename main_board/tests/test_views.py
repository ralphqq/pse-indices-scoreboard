from datetime import datetime

from django.test import TestCase


class MainBoardViewTest(TestCase):
    fixtures = ['value_updates.json']

    def setUp(self):
        self.response = self.client.get('/')

    def test_main_board_view_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'main_board/index.html')

    def test_response_context(self):
        self.assertIsNotNone(
            self.response.context['current_index_values']
        )
        self.assertIsInstance(
            self.response.context['last_update_time'],
            datetime
        )
