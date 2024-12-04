import io
from unittest import TestCase
from unittest.mock import patch
from helpers import display_inventory


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_inventory_one_each_items(self, mock_output):
        character = {'Inventory': {'HP Potion': 1, 'Kibble': 1, 'Key': 1}}
        display_inventory(character)
        actual = mock_output.getvalue()
        expected = (
            "\n🎒 Your Inventory\n"
            "--------------------------------------------------------\n"
            " 1: 🩸 HP Potion (1)   - Fully restores your HP\n"
            " 2: 🍽️ Kibble (1)      - Increases your Hunger by +1\n"
            " 3: 🗝️ Key (1)         - Not directly usable\n"
            "--------------------------------------------------------\n"
        )
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_inventory_five_each_items(self, mock_output):
        character = {'Inventory': {'HP Potion': 5, 'Kibble': 5, 'Key': 5}}
        display_inventory(character)
        actual = mock_output.getvalue()
        expected = (
            "\n🎒 Your Inventory\n"
            "--------------------------------------------------------\n"
            " 1: 🩸 HP Potion (5)   - Fully restores your HP\n"
            " 2: 🍽️ Kibble (5)      - Increases your Hunger by +1\n"
            " 3: 🗝️ Key (5)         - Not directly usable\n"
            "--------------------------------------------------------\n"
        )
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_inventory_various_count_items(self, mock_output):
        character = {'Inventory': {'HP Potion': 3, 'Kibble': 8, 'Key': 1}}
        display_inventory(character)
        actual = mock_output.getvalue()
        expected = (
            "\n🎒 Your Inventory\n"
            "--------------------------------------------------------\n"
            " 1: 🩸 HP Potion (3)   - Fully restores your HP\n"
            " 2: 🍽️ Kibble (8)      - Increases your Hunger by +1\n"
            " 3: 🗝️ Key (1)         - Not directly usable\n"
            "--------------------------------------------------------\n"
        )
        self.assertEqual(actual, expected)
