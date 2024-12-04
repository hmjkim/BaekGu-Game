import io
from unittest import TestCase
from unittest.mock import patch
from helpers import use_kibble


class Test(TestCase):
    def test_use_kibble_greater_than_zero_1_kibble(self):
        character = {'Inventory': {'Kibble': 1}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = character['Inventory']['Kibble']
        expected = 0
        self.assertEqual(actual, expected)

    def test_use_kibble_greater_than_zero_3_kibble(self):
        character = {'Inventory': {'Kibble': 3}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = character['Inventory']['Kibble']
        expected = 2
        self.assertEqual(actual, expected)

    def test_use_kibble_greater_than_zero_check_hunger(self):
        character = {'Inventory': {'Kibble': 3}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = character['Stat']['Hunger']
        expected = 6
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_kibble_greater_than_zero_check_message(self, mock_output):
        character = {'Inventory': {'Kibble': 3}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = mock_output.getvalue()
        expected = "You ate '🍽️Kibble'. Hunger increased by +1. - Remaining quantity: 2\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_kibble_zero_check_message(self, mock_output):
        character = {'Inventory': {'Kibble': 0}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any Kibble.\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_kibble_less_than_zero_check_message(self, mock_output):
        character = {'Inventory': {'Kibble': -1}, 'Stat': {'Hunger': 5}}
        use_kibble(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any Kibble.\n"
        self.assertEqual(actual, expected)
