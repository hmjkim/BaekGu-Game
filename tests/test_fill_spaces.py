from unittest import TestCase
from make_board_each_level import fill_spaces


class Test(TestCase):
    def test_fill_spaces_one(self):
        grid = [[' ' for _ in range(1)] for _ in range(1)]
        expected = [['.']]
        fill_spaces(grid, 1)
        actual = grid
        self.assertEqual(actual, expected)

    def test_fill_spaces_three(self):
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        expected = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        fill_spaces(grid, 3)
        actual = grid
        self.assertEqual(actual, expected)

    def test_fill_spaces_five(self):
        grid = [[' ' for _ in range(5)] for _ in range(5)]
        expected = [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']]
        fill_spaces(grid, 5)
        actual = grid
        self.assertEqual(actual, expected)

    def test_fill_spaces_mixed(self):
        grid = [
            [' ', 'X', ' '],
            ['O', ' ', ' '],
            [' ', ' ', 'P']
        ]
        expected = [
            ['.', 'X', '.'],
            ['O', '.', '.'],
            ['.', '.', 'P']
        ]
        fill_spaces(grid, 3)
        actual = grid
        self.assertEqual(actual, expected)
