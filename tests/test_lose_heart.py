import io
from unittest import TestCase
from unittest.mock import patch
from helpers import lose_heart


class Test(TestCase):
    def test_lose_heart_1_same_hp(self):
        character = {'Stat': {'Heart': 1, 'Current HP': 10, 'HP': 10}}
        lose_heart(character)
        actual = character['Stat']['Heart']
        expected = 0
        self.assertEqual(actual, expected)

    def test_lose_heart_3_same_hp(self):
        character = {'Stat': {'Heart': 3, 'Current HP': 10, 'HP': 10}}
        lose_heart(character)
        actual = character['Stat']['Heart']
        expected = 2
        self.assertEqual(actual, expected)

    def test_lose_heart_negative_heart_same_hp(self):
        character = {'Stat': {'Heart': 0, 'Current HP': 10, 'HP': 10}}
        lose_heart(character)
        actual = character['Stat']['Heart']
        expected = -1
        self.assertEqual(actual, expected)

    def test_lose_heart_3_diff_hp(self):
        character = {'Stat': {'Heart': 3, 'Current HP': 10, 'HP': 20}}
        lose_heart(character)
        actual = character['Stat']['Current HP']
        expected = 20
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lose_heart_3_diff_hp_check_print(self, mock_output):
        character = {'Stat': {'Heart': 3, 'Current HP': 10, 'HP': 20}}
        lose_heart(character)
        actual = mock_output.getvalue()
        expected = '💔 You lost 1 Heart. You have 2 Heart(s) left.\n'
        self.assertEqual(actual, expected)
