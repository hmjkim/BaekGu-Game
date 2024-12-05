from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import check_character_hunger


class TestCheckCharacterHunger(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_character_hunger_zero_hunger(self, mock_output):
        character = {"Stat": {"Hunger": 0, "Max Hunger": 10}}
        check_character_hunger(character)
        print_result = mock_output.getvalue()
        expected_result = ("⚠️⚠️⚠️ Oops! You have run out of energy. It's a nap time, Baekgu ⚠️⚠️⚠️\n"
                           "\n💤 You are going to sleep for 20 second(s) to regain energy."
                           "\n1 sec"
                           "\n2 sec"
                           "\n3 sec"
                           "\n4 sec"
                           "\n5 sec"
                           "\n6 sec"
                           "\n7 sec"
                           "\n8 sec"
                           "\n9 sec"
                           "\n10 sec"
                           "\n11 sec"
                           "\n12 sec"
                           "\n13 sec"
                           "\n14 sec"
                           "\n15 sec"
                           "\n16 sec"
                           "\n17 sec"
                           "\n18 sec"
                           "\n19 sec"
                           "\n20 sec"
                           "\nYou feel well-rested! Your Hunger has been fully restored.\n")
        self.assertEqual(print_result, expected_result)

    def test_check_character_hunger_moderate_hunger(self):
        character = {"Stat": {"Hunger": 5, "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': 5, 'Max Hunger': 10}}
        self.assertEqual(actual, expected)

    def test_check_character_hunger_full_hunger(self):
        character = {"Stat": {"Hunger": 10, "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
        self.assertEqual(actual, expected)

    def test_check_character_hunger_excessive_hunger(self):
        character = {"Stat": {"Hunger": 15, "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': 15, 'Max Hunger': 10}}
        self.assertEqual(actual, expected)

    def test_check_character_hunger_invalid_hunger(self):
        character = {"Stat": {"Hunger": 'a', "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': 'a', 'Max Hunger': 10}}
        self.assertEqual(actual, expected)

    def test_check_character_hunger_negative_hunger(self):
        character = {"Stat": {"Hunger": -5, "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': -5, 'Max Hunger': 10}}
        self.assertEqual(actual, expected)

    def test_check_character_hunger_fully_restored_hunger_after_sleep(self):
        character = {"Stat": {"Hunger": 0, "Max Hunger": 10}}
        actual = check_character_hunger(character)
        expected = {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
        self.assertEqual(actual, expected)
