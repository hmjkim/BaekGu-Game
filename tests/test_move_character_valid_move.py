from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import move_character_valid_move


class TestMoveCharacterValidMove(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_valid_move_right(self, mock_output):
        grid = [
            ['#', '#', '#', '#'],
            ['#', '.', '🐶', '.'],
            ['#', '.', '.', '#'],
            ['#', '#', '#', '#']
        ]
        position = (1, 2)
        direction = 'd'
        prev_cell_content = '.'
        character = {"Stat": {"Hunger": 10}}

        new_position, new_prev_cell_content, updated_character, valid_check = move_character_valid_move(
            grid, position, direction, prev_cell_content, character)

        print_result = mock_output.getvalue()
        expected_result = "You moved one step right. Everything seems quiet.\n"
        self.assertEqual(print_result, expected_result)
