from io import StringIO
from unittest import TestCase
from unittest.mock import patch, mock_open

from game import check_user


class TestCheckUser(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_user_new_user_message(self, mock_output, _):
        check_user('sleepy')
        print_result = mock_output.getvalue()
        expected_result = '✅ New user is created!\n'
        self.assertEqual(print_result, expected_result)

    @patch('builtins.open', new_callable=mock_open, read_data="Heather")
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_user_returning_user_message(self, mock_output, _):
        check_user('Heather')
        print_result = mock_output.getvalue()
        expected_result = "You're already a player! Welcome back, Heather!\n"
        self.assertEqual(print_result, expected_result)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_check_user_is_new_user(self, _):
        actual = check_user('Newbie')
        expected = False
        self.assertEqual(actual, expected)

    @patch('builtins.open', new_callable=mock_open, read_data="Heather")
    def test_check_user_is_returning_user(self, _):
        actual = check_user('Heather')
        expected = True
        self.assertEqual(actual, expected)
