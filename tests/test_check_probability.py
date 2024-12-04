from unittest import TestCase
from unittest.mock import patch

from game import check_probability


class TestCheckProbability(TestCase):

    @patch('random.random', return_value=0.8)
    def test_check_probability_always_occur(self, _):
        actual = check_probability(1.0)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.random', return_value=0.9)
    def test_check_probability_not_occur(self, _):
        actual = check_probability(0.5)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.random', return_value=0.4)
    def test_check_probability_occur_at_50_percent_chance(self, _):
        actual = check_probability(0.5)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.random', return_value=0.05)
    def test_check_probability_occur_at_10_percent_chance(self, _):
        actual = check_probability(0.1)
        expected = True
        self.assertEqual(actual, expected)
