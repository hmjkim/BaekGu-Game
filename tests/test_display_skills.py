import io
from unittest import TestCase
from unittest.mock import patch
from helpers import display_skills


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_skills_exist_skills(self, mock_output):
        character = {
            "Skill": {
                "Current Skills": {
                    "Bark": {"Damage": 25, "Description": "A quick slash"},
                    "Bite": {"Damage": 30, "Description": "A sharp stab"},
                }
            }
        }
        display_skills(character)
        actual = mock_output.getvalue()
        expected = "\n⚔️ Your Skills\n" + \
                   "--------------------------------------------------------\n" + \
                   "Bark        : Damage: 25, A quick slash\n" + \
                   "Bite        : Damage: 30, A sharp stab\n" + \
                   "--------------------------------------------------------\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_skills_empty_skills(self, mock_output):
        character = {
            "Skill": {
                "Current Skills": {
                }
            }
        }
        display_skills(character)
        actual = mock_output.getvalue()
        expected = "\n⚔️ Your Skills\n" + \
                   "--------------------------------------------------------\n" + \
                   "--------------------------------------------------------\n"
        self.assertEqual(actual, expected)
