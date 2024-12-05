from unittest import TestCase
from game import check_character_2_level_location_exp


class Test(TestCase):
    def test_check_character_2_level_location_exp_meets_requirements(self):
        character = {
            'Inventory': {'Key': 3},
            'Stat': {
                'Level': 2,
                'Exp': 1350,
                'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}
            }
        }
        actual = check_character_2_level_location_exp((4, 8), character)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_character_2_level_location_exp_wrong_location(self):
        character = {
            'Inventory': {'Key': 3},
            'Stat': {
                'Level': 2,
                'Exp': 1350,
                'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}
            }
        }
        actual = check_character_2_level_location_exp((3, 8), character)
        expected = None
        self.assertEqual(actual, expected)

    def test_check_character_2_level_location_exp_missing_key(self):
        character = {
            'Inventory': {'Key': 0},
            'Stat': {
                'Level': 2,
                'Exp': 1350,
                'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}
            }
        }
        actual = check_character_2_level_location_exp((4, 8), character)
        expected = None
        self.assertEqual(actual, expected)

    def test_check_character_2_level_location_exp_insufficient_exp(self):
        character = {
            'Inventory': {'Key': 3},
            'Stat': {
                'Level': 2,
                'Exp': 1200,
                'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}
            }
        }
        actual = check_character_2_level_location_exp((4, 8), character)
        expected = None
        self.assertEqual(actual, expected)

    def test_check_character_2_level_location_exp_wrong_level(self):
        character = {
            'Inventory': {'Key': 3},
            'Stat': {
                'Level': 1,
                'Exp': 1350,
                'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500}
            }
        }
        actual = check_character_2_level_location_exp((4, 8), character)
        expected = None
        self.assertEqual(actual, expected)

