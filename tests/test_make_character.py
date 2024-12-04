from unittest import TestCase
from unittest.mock import patch

from game import make_character


class TestMakeCharacter(TestCase):

    def test_make_character_contains_stat_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Stat', character)

    def test_make_character_contains_HP_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('HP', character['Stat'])

    def test_make_character_contains_current_HP_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Current HP', character['Stat'])

    def test_make_character_contains_level_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Level', character['Stat'])

    def test_make_character_contains_exp_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Exp', character['Stat'])

    def test_make_character_contains_max_exp_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Max Exp', character['Stat'])

    def test_make_character_contains_heart_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Heart', character['Stat'])

    def test_make_character_contains_hunger_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Hunger', character['Stat'])

    def test_make_character_contains_max_hunger_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Max Hunger', character['Stat'])

    def test_make_character_contains_skill_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Skill', character)

    def test_make_character_contains_level_1_skill(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Bark', character['Skill']['Current Skills'])

    def test_make_character_contains_inventory_key(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        self.assertIn('Inventory', character)

    def test_make_character_current_hp_is_250(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        actual = character['Stat']['Current HP']
        expected = 250
        self.assertEqual(actual, expected)

    def test_make_character_current_hunger_is_10(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        actual = character['Stat']['Hunger']
        expected = 10
        self.assertEqual(actual, expected)

    def test_make_character_current_heart_is_10(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        actual = character['Stat']['Heart']
        expected = 10
        self.assertEqual(actual, expected)

    def test_make_character_has_no_hp_potion(self):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        actual = character['Inventory']['HP Potion']
        expected = 0
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=20)
    def test_make_character_basic_attack_within_range(self, _):
        skill_set = {'Level 1': {'Bark': {'Damage': 25, 'Description': 'A loud bark that stuns the enemy'}}}
        character = make_character(skill_set)
        actual = character['Skill']['Basic Attack']
        expected = 20
        self.assertEqual(actual, expected)
