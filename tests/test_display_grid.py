import io
from unittest import TestCase
from unittest.mock import patch
from make_board_each_level import display_grid


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_grid_empty(self, mock_output):
        grid = []
        display_grid(grid)
        actual = mock_output.getvalue()
        expected = ''
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_grid_one(self, mock_output):
        grid = [['#']]
        display_grid(grid)
        actual = mock_output.getvalue()
        expected = '#\n'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_grid_three(self, mock_output):
        grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        display_grid(grid)
        actual = mock_output.getvalue()
        expected = '. . .\n. . .\n. . .\n'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_grid_three_with_wall(self, mock_output):
        grid = [['#', '#', '.'], ['.', '#', '.'], ['.', '.', '#']]
        display_grid(grid)
        actual = mock_output.getvalue()
        expected = '# # .\n. # .\n. . #\n'
        self.assertEqual(actual, expected)



