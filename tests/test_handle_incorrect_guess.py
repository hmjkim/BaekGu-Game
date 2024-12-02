import io
from unittest import TestCase
from unittest.mock import patch
from hangman import handle_incorrect_guess


class Test(TestCase):
    def test_handle_incorrect_guess_check_list(self):
        guess = 'x'
        incorrect_guesses = []
        remaining_lives = 5
        handle_incorrect_guess(guess, incorrect_guesses, remaining_lives)
        expected = ['x']
        self.assertEqual(expected, incorrect_guesses)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_incorrect_guess_check_remaining_lives(self, mock_output):
        guess = 'x'
        incorrect_guesses = []
        remaining_lives = 5
        handle_incorrect_guess(guess, incorrect_guesses, remaining_lives)
        expected = 'Current lives: 5'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_incorrect_guess_message(self, mock_output):
        guess = 'x'
        incorrect_guesses = []
        remaining_lives = 5
        handle_incorrect_guess(guess, incorrect_guesses, remaining_lives)
        expected = "You guessed 'x'"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_incorrect_check_word_strike_function_works(self, mock_output):
        guess = 'x'
        incorrect_guesses = []
        remaining_lives = 5
        handle_incorrect_guess(guess, incorrect_guesses, remaining_lives)
        expected = "Incorrect answers: ̶x"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
