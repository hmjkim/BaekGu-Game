from unittest import TestCase
from helpers import is_alive


class Test(TestCase):
    def test_is_alive_heart_0(self):
        character = {'Stat': {'Heart': 0}}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_heart_1(self):
        character = {'Stat': {'Heart': 1}}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_heart_5(self):
        character = {'Stat': {'Heart': 5}}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_heart_negative(self):
        character = {'Stat': {'Heart': -1}}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)
