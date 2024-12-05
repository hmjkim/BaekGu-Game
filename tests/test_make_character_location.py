from unittest import TestCase
from game import make_character_location


class Test(TestCase):
    def test_make_character_location_only_dot_check_map(self):
        grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        make_character_location(grid)
        actual = grid
        expected = [['.', '.', '.'], ['.', '🐶', '.'], ['.', '.', '.']]
        self.assertEqual(actual, expected)

    def test_make_character_location_only_dot_check_returns(self):
        grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        first_pre_content = make_character_location(grid)
        actual = first_pre_content
        expected = ((1, 1), '.')
        self.assertEqual(actual, expected)

    def test_make_character_location_mixed_map_check_map(self):
        grid = [['!', '.', '#'], ['l', '.', 'x'], ['a', 'b', '.']]
        make_character_location(grid)
        actual = grid
        expected = [['!', '.', '#'], ['l', '🐶', 'x'], ['a', 'b', '.']]
        self.assertEqual(actual, expected)

    def test_make_character_location_mixed_map_check_returns(self):
        grid = [['!', '.', '#'], ['l', '.', 'x'], ['a', 'b', '.']]
        first_pre_content = make_character_location(grid)
        actual = first_pre_content
        expected = ((1, 1), '.')
        self.assertEqual(actual, expected)
