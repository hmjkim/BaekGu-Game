from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import level_up


class TestLevelUp(TestCase):

    def test_level_up_to_2(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 1,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 2': {'Digging': {'Damage': 40, 'Description': 'Kick up dirt to blind the enemy'}}}
        level_up(character, 250, 2, skill_set)
        actual = character['Stat']['Level']
        expected = 2
        self.assertEqual(actual, expected)

    def test_level_up_to_3(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Stat']['Level']
        expected = 3
        self.assertEqual(actual, expected)

    def test_level_up_key_reset(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Inventory']['Key']
        expected = 0
        self.assertEqual(actual, expected)

    def test_level_up_hunger_restored_to_10(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Stat']['Hunger']
        expected = 10
        self.assertEqual(actual, expected)

    def test_level_up_max_hp_increased(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Stat']['HP']
        expected = 650
        self.assertEqual(actual, expected)

    def test_level_up_current_hp_restored(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Stat']['Current HP']
        expected = 650
        self.assertEqual(actual, expected)

    def test_level_up_exp_reset(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 1000,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Stat']['Exp']
        expected = 0
        self.assertEqual(actual, expected)

    def test_level_up_basic_attack_damage_increased(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Skill']['Basic Attack']
        expected = 25
        self.assertEqual(actual, expected)

    def test_level_up_new_skills_added(self):
        character = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 2,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {"Key": 5},
            "Skill": {
                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 3': {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}}
        level_up(character, 400, 3, skill_set)
        actual = character['Skill']['Current Skills']
        expected = {'Bite': {'Damage': 56, 'Description': 'A strong bite with a headshake'}}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_up_print_informative_message(self, mock_output):
        character_ready_to_level_up = {
            "Stat": {
                "HP": 250,
                "Current HP": 250,
                "Level": 1,
                "Exp": 0,
                "Heart": 10,
                "Hunger": 3},
            "Inventory": {

                "Key": 5},
            "Skill": {

                "Basic Attack": 20,
                "Current Skills": {}
            }
        }
        skill_set = {'Level 2': {'Digging': {'Damage': 40,
                                             'Description': 'Kick up dirt to blind the enemy'},
                                 'Scratch': {'Damage': 45,
                                             'Description': 'A swift paw swipe leaving deep '
                                                            'marks'}}}
        level_up(character_ready_to_level_up, 250, 2, skill_set)
        print_result = mock_output.getvalue()
        expected_result = ('Your maximum HP has been increased by 250. You earned two new skills (Digging,Scratch). '
                           '(max HP +250)\n\n')
        self.assertEqual(print_result, expected_result)
