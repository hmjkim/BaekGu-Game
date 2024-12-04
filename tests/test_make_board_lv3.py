from unittest import TestCase
from make_board_each_level import make_board_lv3


class Test(TestCase):
    def test_make_board_lv3_map(self):
        actual = make_board_lv3()
        expected = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '.', '.', '.', '#'],
                    ['#', '.', '.', '.', '!', '#', '.', '.', '.', '#'],
                    ['#', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
                    ['#', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
                    ['#', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.assertEqual(actual, expected)

    def test_make_board_lv3_check_mark(self):
        grid = make_board_lv3()
        actual = grid[4][4]
        expected = '!'
        self.assertEqual(actual, expected)
