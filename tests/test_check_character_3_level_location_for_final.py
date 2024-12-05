from unittest import TestCase
from unittest.mock import patch
from game import check_character_3_level_location_for_final


class Test(TestCase):
    @patch('game.battle')
    def test_character_fights_final_boss(self, mock_battle):
        character = {
            'Stat': {
                'Level': 3,
                'Exp': 100,
                'Max Exp': {'Level 3': 100}
            }
        }
        mock_battle.return_value = (character, True)
        result = check_character_3_level_location_for_final((4, 4), character)
        self.assertTrue(result)

    @patch('game.battle')
    def test_character_not_fights_wrong_location(self, mock_battle):
        character = {
            'Stat': {
                'Level': 3,
                'Exp': 100,
                'Max Exp': {'Level 3': 100}
            }
        }
        result = check_character_3_level_location_for_final((3, 3), character)
        self.assertFalse(result)
        mock_battle.assert_not_called()

    @patch('game.battle')
    def test_character_not_fights_insufficient_exp(self, mock_battle):
        character = {
            'Stat': {
                'Level': 3,
                'Exp': 50,
                'Max Exp': {'Level 3': 100}
            }
        }
        result = check_character_3_level_location_for_final((4, 4), character)
        self.assertFalse(result)
        mock_battle.assert_not_called()

    @patch('game.battle')
    def test_character_not_fights_wrong_level(self, mock_battle):
        character = {
            'Stat': {
                'Level': 2,
                'Exp': 100,
                'Max Exp': {'Level 3': 100}
            }
        }
        result = check_character_3_level_location_for_final((4, 4), character)
        self.assertFalse(result)
        mock_battle.assert_not_called()
