from unittest import TestCase
from make_board_each_level import make_board_lv2


class Test(TestCase):
    def test_make_board_lv2_map(self):
        actual = make_board_lv2()
        expected = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '.', '#', '#', '#', '.', '.', '.', '.', '#'],
                    ['#', '.', '#', '#', '#', '.', '.', '.', '.', '#'],
                    ['#', '.', '.', '#', '#', '.', '.', '#', '!', '#'],
                    ['#', '.', '.', '#', '#', '.', '.', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.assertEqual(actual, expected)

    def test_make_board_lv2_check_mark(self):
        grid = make_board_lv2()
        actual = grid[4][8]
        expected = '!'
        self.assertEqual(actual, expected)
