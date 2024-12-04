from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from minigames.battle import display_attack_description


class TestDisplayAttackDescription(TestCase):

    @patch('random.choice',
           return_value="🗡️ With a focused attack, you manage to break through the enemy's guard, causing visible pain!")
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_attack_description_correctly_replace_enemy_name(self, mock_output, _):
        display_attack_description('Spider')
        print_result = mock_output.getvalue()
        expected_result = "🗡️ With a focused attack, you manage to break through the Spider's guard, causing visible pain!\n"
        self.assertEqual(print_result, expected_result)

    @patch('random.choice',
           return_value="🗡️ With a focused attack, you manage to break through the enemy's guard, causing visible pain!")
    def test_display_attack_description_empty_name_valueerror(self, _):
        with self.assertRaises(ValueError):
            display_attack_description('')

    @patch('random.choice',
           return_value="🗡️ With a focused attack, you manage to break through the enemy's guard, causing visible pain!")
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_attack_description_name_with_punctuation(self, mock_output, _):
        display_attack_description('Spider**!')
        print_result = mock_output.getvalue()
        expected_result = "🗡️ With a focused attack, you manage to break through the Spider**!'s guard, causing visible pain!\n"
        self.assertEqual(print_result, expected_result)

    @patch('random.choice',
           return_value="🗡️ With a focused attack, you manage to break through the enemy's guard, causing visible pain!")
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_attack_description_with_long_name(self, mock_output, _):
        display_attack_description('Spider with Fierce Eyes and Sticky Web around Itself')
        print_result = mock_output.getvalue()
        expected_result = "🗡️ With a focused attack, you manage to break through the Spider with Fierce Eyes and Sticky Web around Itself's guard, causing visible pain!\n"
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_attack_description_get_from_predefined_list(self, mock_output):
        attack_descriptions = [
            "🗡️ You strike fiercely, leaving a mark on the Spider!",
            "🗡️ Your attack lands cleanly, leaving the Spider struggling to recover!",
            "🗡️ With a focused attack, you manage to break through the Spider's guard, causing visible pain!",
            "🗡️ Your powerful attack stunned the Spider.",
            "🗡️ Your strike pierced through the Spider with precision."
        ]
        display_attack_description('Spider')
        print_result = mock_output.getvalue().strip()
        self.assertIn(print_result, attack_descriptions)
