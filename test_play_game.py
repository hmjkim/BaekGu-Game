from unittest import TestCase
from unittest.mock import patch
from matching_direction_game import play_game


class Test(TestCase):
    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    @patch('builtins.input', side_effect=['A', 'D', 'S', 'W'])
    def test_play_game_success_boolean(self, _, __):
        character = {'Stat': {'Heart': 1}}
        level = 4
        actual, updated_character = play_game(level, character)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    @patch('builtins.input', side_effect=['A', 'D', 'S', 'W'])
    def test_play_game_success_save_heart(self, _, __):
        character = {'Stat': {'Heart': 1}}
        level = 4
        result, actual = play_game(level, character)
        expected = {'Stat': {'Heart': 1}}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['W', 'S', 'D', 'A'])
    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    def test_play_game_failure_boolean(self, _, __):
        character = {'Stat': {'Heart': 3}}
        level = 4
        actual, updated_character = play_game(level, character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['W', 'S', 'D', 'A'])
    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    def test_play_game_failure_reduce_heart(self, _, __):
        character = {'Stat': {'Heart': 3}}
        level = 4
        result, actual = play_game(level, character)
        expected = {'Stat': {'Heart': 2}}
        self.assertEqual(actual, expected)
