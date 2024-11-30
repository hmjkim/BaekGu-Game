from unittest import TestCase
from matching_direction_game import check_character_level_matching_game


class Test(TestCase):
    def test_check_character_level_matching_game_level1(self):
        character = {'Stat': {'Level': 1}}
        actual = check_character_level_matching_game(character)
        expected = 5
        self.assertEqual(actual, expected)
    def test_check_character_level_matching_game_level2(self):
        character = {'Stat': {'Level': 2}}
        actual = check_character_level_matching_game(character)
        expected = 7
        self.assertEqual(actual, expected)

    def test_check_character_level_matching_game_level3(self):
        character = {'Stat': {'Level': 3}}
        actual = check_character_level_matching_game(character)
        expected = 9
        self.assertEqual(actual, expected)

    def test_check_character_level_matching_game_level4(self):
        character = {'Stat': {'Level': 4}}
        actual = check_character_level_matching_game(character)
        expected = 9
        self.assertEqual(actual, expected)
