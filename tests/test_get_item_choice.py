import io
from unittest import TestCase
from unittest.mock import patch
from helpers import get_item_choice


class Test(TestCase):
    @patch('builtins.input', side_effect=['1', 'q'])
    def test_get_item_choice_use_hp_potion(self, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = character['Stat']['Current HP']
        expected = 20
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', 'q'])
    def test_get_item_choice_check_hp_potion(self, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = character['Inventory']['HP Potion']
        expected = 0
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_choice_check_hp_potion_zero(self, mock_output, _):
        character = {'Inventory': {'HP Potion': 0, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any HP Potion.\n"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2', 'q'])
    def test_get_item_choice_use_kibble(self, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = character['Stat']['Hunger']
        expected = 6
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2', 'q'])
    def test_get_item_choice_check_kibble(self, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = character['Inventory']['Kibble']
        expected = 0
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_choice_check_kibble_zero(self, mock_output, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 0, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = mock_output.getvalue()
        expected = "❌ You don't have any Kibble.\n"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_choice_check_key_use(self, mock_output, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = mock_output.getvalue()
        expected = "❌ You cannot directly use the key. The key will be automatically used at the door.\n"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='q')
    def test_get_item_choice_check_quit(self, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        actual = get_item_choice(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['k', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_choice_check_invalid_input(self, mock_output, _):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1},
                     'Stat': {'Current HP': 10, 'HP': 20, 'Hunger': 5}}
        get_item_choice(character)
        actual = mock_output.getvalue()
        expected = "❌ Invalid input. Please enter a correct option from the list.\n"
        self.assertEqual(actual, expected)
