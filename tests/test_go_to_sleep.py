from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import go_to_sleep


class TestGoToSleep(TestCase):

    def test_go_to_sleep_fully_restore_hunger_when_low_hunger(self):
        character = {"Stat": {
            "Hunger": 1,
            "Max Hunger": 10
        }}
        go_to_sleep(character, 10)
        actual = character["Stat"]["Hunger"]
        expected = 10
        self.assertEqual(actual, expected)

    def test_go_to_sleep_fully_restore_hunger_when_full_hunger(self):
        character = {"Stat": {
            "Hunger": 10,
            "Max Hunger": 10
        }}
        go_to_sleep(character, 10)
        actual = character["Stat"]["Hunger"]
        expected = 10
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_go_to_sleep_suspend_execution_for_5_sec(self, mock_output):
        character = {"Stat": {
            "Hunger": 10,
            "Max Hunger": 10
        }}
        go_to_sleep(character, 5)
        print_result = mock_output.getvalue()
        expected_result = ('\n💤 You are going to sleep for 10 second(s) to regain energy.'
                           '\n1 sec'
                           '\n2 sec'
                           '\n3 sec'
                           '\n4 sec'
                           '\n5 sec'
                           '\nYou feel well-rested! Your Hunger has been fully restored.\n')
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_go_to_sleep_suspend_execution_for_1_sec(self, mock_output):
        character = {"Stat": {
            "Hunger": 10,
            "Max Hunger": 10
        }}
        go_to_sleep(character, 1)
        print_result = mock_output.getvalue()
        expected_result = ('\n💤 You are going to sleep for 1 second(s) to regain energy.'
                           '\n1 sec'
                           '\nYou feel well-rested! Your Hunger has been fully restored.\n')
        self.assertEqual(print_result, expected_result)
