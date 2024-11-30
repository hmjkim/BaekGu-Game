from unittest import TestCase


class Test(TestCase):
    def test_play_game(self):
        self.fail()






from unittest.mock import patch

from matching_direction_game import play_game


class TestPlayGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['A', 'D', 'S', 'W'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    def test_play_game_success(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 3}}
        level = 4

        result, updated_character = play_game(level, character)

        self.assertTrue(result)
        self.assertEqual(updated_character['Stat']['Heart'], 3)

    @patch('builtins.input', side_effect=['W', 'S', 'D', 'A'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['A', 'D', 'S', 'W'])
    def test_play_game_failure(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 3}}
        level = 4

        result, updated_character = play_game(level, character)

        self.assertFalse(result)
        self.assertEqual(updated_character['Stat']['Heart'], 2)

    @patch('builtins.input', side_effect=['A', 'S', 'W', 'D'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['A', 'S', 'W', 'D'])
    def test_play_game_success_edge_case(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 1}}
        level = 4

        result, updated_character = play_game(level, character)

        self.assertTrue(result)
        self.assertEqual(updated_character['Stat']['Heart'], 1)

    @patch('builtins.input', side_effect=['A', 'D', 'W', 'S'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['S', 'W', 'D', 'A'])
    def test_play_game_failure_edge_case(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 5}}
        level = 4

        result, updated_character = play_game(level, character)

        self.assertFalse(result)
        self.assertEqual(updated_character['Stat']['Heart'], 4)

    @patch('builtins.input', side_effect=['S', 'S'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['S', 'S'])
    def test_play_game_multiple_same_directions_success(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 2}}
        level = 2

        result, updated_character = play_game(level, character)

        self.assertTrue(result)
        self.assertEqual(updated_character['Stat']['Heart'], 2)

    @patch('builtins.input', side_effect=['D', 'D', 'D'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['D', 'S', 'D'])
    def test_play_game_multiple_same_directions_failure(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 4}}
        level = 3

        result, updated_character = play_game(level, character)

        self.assertFalse(result)
        self.assertEqual(updated_character['Stat']['Heart'], 3)

    @patch('builtins.input', side_effect=['A', 'A', 'A'])
    @patch('builtins.print')
    @patch('random.choices', return_value=['D', 'D', 'D'])
    def test_play_game_all_incorrect_inputs(self, mock_random_choices, mock_print, mock_input):
        character = {'Stat': {'Heart': 6}}
        level = 3

        result, updated_character = play_game(level, character)

        self.assertFalse(result)
        self.assertEqual(updated_character['Stat']['Heart'], 5)

