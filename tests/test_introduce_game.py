from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import introduce_game


class TestIntroduceGame(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_game_greet_with_player_name(self, mock_output):
        introduce_game('Heather')
        print_result = mock_output.getvalue()
        expected_result = 'Welcome to Baekgu, Heather!'
        self.assertIn(expected_result, print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_game_user_name_has_punctuation(self, mock_output):
        introduce_game('@meow')
        print_result = mock_output.getvalue()
        expected_result = 'Welcome to Baekgu, @meow!'
        self.assertIn(expected_result, print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_game_user_name_has_whitespaces(self, mock_output):
        introduce_game('      ')
        print_result = mock_output.getvalue()
        expected_result = 'Welcome to Baekgu,       !'
        self.assertIn(expected_result, print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_game_user_name_has_a_whitespace_between_characters(self, mock_output):
        introduce_game('Young Bin')
        print_result = mock_output.getvalue()
        expected_result = 'Welcome to Baekgu, Young Bin!'
        self.assertIn(expected_result, print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_game_user_display_story(self, mock_output):
        introduce_game('user')
        print_result = mock_output.getvalue()
        expected_result = 'You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family.'
        self.assertIn(expected_result, print_result)
