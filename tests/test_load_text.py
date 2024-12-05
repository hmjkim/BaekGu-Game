from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from game import load_text


class TestLoadText(TestCase):

    def test_load_text_read_correct_file(self):
        content = load_text('../intro.txt')
        actual = content[:4]
        expected = ['You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond '
                    'with your family.',
                    'Life has always been happy, full of love and play, until today—something is '
                    'terribly wrong.',
                    "Using your extraordinary sense of smell and intuition, you've realized that "
                    "your family's little boy, Haru, has suddenly gone missing.",
                    "Your mission is clear - Find Haru and bring him back home safely before it's "
                    'too late.']
        self.assertEqual(actual, expected)

    def test_load_text_file_with_empty_content(self):
        actual = load_text('empty.txt')
        expected = []
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_load_text_filenotfounderror(self, mock_output):
        load_text('example')
        print_result = mock_output.getvalue()
        expected_output = "Error: The file example was not found.\n"
        self.assertEqual(print_result, expected_output)

    def test_load_text_trailing_newline_character_removed(self):
        content = load_text('../intro.txt')
        first_line = content[0]
        actual = first_line.endswith('\n')
        expected = False
        self.assertEqual(actual, expected)
