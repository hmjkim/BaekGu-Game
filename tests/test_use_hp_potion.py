import io
from unittest import TestCase
from unittest.mock import patch
from helpers import use_hp_potion


class Test(TestCase):
    def test_use_hp_potion_grater_than_zero_1_potion(self):
        character = {'Inventory': {'HP Potion': 1}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = character['Inventory']['HP Potion']
        expected = 0
        self.assertEqual(actual, expected)

    def test_use_hp_potion_grater_than_zero_3_potion(self):
        character = {'Inventory': {'HP Potion': 3}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = character['Inventory']['HP Potion']
        expected = 2
        self.assertEqual(actual, expected)

    def test_use_hp_potion_grater_than_zero_check_diff_hp(self):
        character = {'Inventory': {'HP Potion': 3}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = character['Stat']['Current HP']
        expected = 100
        self.assertEqual(actual, expected)

    def test_use_hp_potion_grater_than_zero_check_same_hp(self):
        character = {'Inventory': {'HP Potion': 3}, 'Stat': {'Current HP': 100, 'HP': 100}}
        use_hp_potion(character)
        actual = character['Stat']['Current HP']
        expected = 100
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_hp_potion_grater_than_zero_check_message(self, mock_output):
        character = {'Inventory': {'HP Potion': 3}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = mock_output.getvalue()
        expected = "You used '🩸HP Potion'. Your HP is fully restored now. (HP 100/100) - Remaining quantity: 2\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_hp_potion_zero_potion(self, mock_output):
        character = {'Inventory': {'HP Potion': 0}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any HP Potion.\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_hp_potion_less_than_zero_potion(self, mock_output):
        character = {'Inventory': {'HP Potion': -1}, 'Stat': {'Current HP': 50, 'HP': 100}}
        use_hp_potion(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any HP Potion.\n"
        self.assertEqual(actual, expected)
