from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from minigames.battle import show_current_hp


class TestShowCurrentHP(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_is_0(self, mock_output):
        show_current_hp(0, 100, 'Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Spider HP: 0/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_is_negative(self, mock_output):
        show_current_hp(-80, 100, 'Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Spider HP: 0/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_is_positive(self, mock_output):
        show_current_hp(80, 100, 'Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Spider HP: 80/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_original_hp_is_positive(self, mock_output):
        show_current_hp(100, 100, 'Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Spider HP: 100/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_name_is_character(self, mock_output):
        show_current_hp(20, 100, 'Your')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Your HP: 20/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_name_is_enemy(self, mock_output):
        show_current_hp(1, 100, 'Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 Spider HP: 1/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_name_has_punctuation(self, mock_output):
        show_current_hp(1, 100, '@Spider')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸 @Spider HP: 1/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_current_hp_name_is_empty(self, mock_output):
        show_current_hp(1, 100, '')
        print_result = mock_output.getvalue()
        expected_result = '*** 🩸  HP: 1/100 ***\n\n'
        self.assertEqual(print_result, expected_result)

    def test_show_current_hp_true_when_0(self):
        actual = show_current_hp(0, 100, 'Your')
        expected = True
        self.assertEqual(actual, expected)

    def test_show_current_hp_true_when_negative(self):
        actual = show_current_hp(-39, 100, 'Your')
        expected = True
        self.assertEqual(actual, expected)

    def test_show_current_hp_false_when_positive(self):
        actual = show_current_hp(30, 100, 'Your')
        expected = False
        self.assertEqual(actual, expected)
