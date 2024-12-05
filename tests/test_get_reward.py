from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import get_reward, check_probability


class TestGetReward(TestCase):

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, False, False, False, False, False])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_reward_print_reward_list(self, mock_output, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        get_reward(character)
        print_result = mock_output.getvalue()
        expected_result = ("🏆 Reward Earned 🏆\n"
                           " - Exp +304          (304/1000)\n")
        self.assertEqual(print_result, expected_result)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, False, False, False, False, False])
    def test_get_reward_exp_updated(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Stat']['Exp']
        expected = 304
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, False, False, False, False, True])
    def test_get_reward_key_saved_to_inventory(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Inventory']['Key']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, True, False, False, False, False])
    def test_get_reward_hp_potion_saved_to_inventory(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Inventory']['HP Potion']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, False, False, True, False, False])
    def test_get_reward_kibble_saved_to_inventory(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Inventory']['Kibble']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[True, False, False, False, False, False])
    def test_get_reward_basic_attack_damage_increased(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Skill']['Basic Attack']
        expected = 50
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=304)
    @patch('game.check_probability', side_effect=[False, False, True, False, False, False])
    def test_get_reward_max_hp_increased(self, _, __):
        character = {
            "Stat": {
                "HP": 500,
                "Current HP": 100,
                "Level": 1,
                "Exp": 0,
                "Hunger": 3,
                "Max Exp": {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
            },
            "Skill": {
                "Basic Attack": 20
            },
            "Inventory": {
                "HP Potion": 0,
                "Key": 0,
                "Kibble": 0
            }
        }
        new_character = get_reward(character)
        actual = new_character['Stat']['HP']
        expected = 600
        self.assertEqual(actual, expected)
