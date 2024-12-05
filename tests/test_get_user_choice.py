from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=['1', 'd'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_1_directions(self, mock_output, _):
        character = {'Stat': {'HP': 250, 'Current HP': 250, 'Level': 1, 'Exp': 0,
                              'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}, 'Heart': 10,
                              'Max Heart': 10, 'Hunger': 10, 'Max Hunger': 10}, 'Skill': {'Basic Attack': 29,
                                                                                          'Current Skills': {
                                                                                              'Bark': {'Damage': 29,
                                                                                                       'Description': 'A loud bark that stuns the enemy'}}},
                     'Inventory': {'Key': 0, 'HP Potion': 0, 'Kibble': 0}}
        grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '🐶', '.', '.', '.', '.', '.', '.', '#', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['#', '#', '#', '#', '#', '#', '.', '.', '.', '#'], ['#', '!', '.', '.', '#', '#', '.', '#', '#', '#'],
                ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        get_user_choice(character, grid)
        print_result = mock_output.getvalue()
        expected_result = """
# # # # # # # # # #
# 🐶 . . . . . . # #
# # # # # # # . . #
# # # # # # # # . #
# # # # # # # # . #
# # # # # # # # . #
# # # # # # . . . #
# ! . . # # . # # #
# . . . . . . # # #
# # # # # # # # # #

🐕 Directions Available:
W : Up
A : Left
S : Down
D : Right"""
        self.assertEqual(print_result.strip(), expected_result.strip())
