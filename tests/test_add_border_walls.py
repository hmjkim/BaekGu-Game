from unittest import TestCase
from make_board_each_level import add_border_walls


class Test(TestCase):
    def test_add_border_walls_empty(self):
        grid = []
        expected = []
        actual = add_border_walls(grid, 0)
        self.assertEqual(actual, expected)

    def test_add_border_walls_size_1(self):
        grid = [[' ' for _ in range(1)] for _ in range(1)]
        expected = [['#']]
        actual = add_border_walls(grid, 1)
        self.assertEqual(actual, expected)

    def test_add_border_walls_size_3(self):
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        expected = [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']]
        actual = add_border_walls(grid, 3)
        self.assertEqual(actual, expected)

    def test_add_border_walls_size_4(self):
        grid = [[' ' for _ in range(4)] for _ in range(4)]
        expected = [['#', '#', '#', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', ' ', ' ', '#'],
                    ['#', '#', '#', '#']]
        actual = add_border_walls(grid, 4)
        self.assertEqual(actual, expected)
