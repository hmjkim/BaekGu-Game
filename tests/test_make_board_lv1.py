from unittest import TestCase
from make_board_each_level import make_board_lv1


class Test(TestCase):
    def test_make_board_lv1_map(self):
        actual = make_board_lv1()
        expected = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '.', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '.', '.', '.', '#'],
                    ['#', '!', '.', '.', '#', '#', '.', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.assertEqual(actual, expected)

    def test_make_board_lv1_check_mark(self):
        grid = make_board_lv1()
        actual = grid[7][1]
        expected = '!'
        self.assertEqual(actual, expected)
