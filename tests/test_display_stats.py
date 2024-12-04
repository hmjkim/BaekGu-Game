import io
from unittest import TestCase
from unittest.mock import patch
from helpers import display_stats


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level1_check_level(self, mock_output):
        character = {
            'Stat': {
                'Level': 1,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Level          : 1\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_level(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Level          : 2\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_hp(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'HP             : 30/50\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_Exp(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Exp            : 10/200\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_Hearts(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Hearts         : 1/5\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_Hunger(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Hunger         : 3/10\n'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats_level2_check_attack(self, mock_output):
        character = {
            'Stat': {
                'Level': 2,
                'Current HP': 30,
                'HP': 50,
                'Exp': 10,
                'Max Exp': {'Level 1': 100, 'Level 2': 200},
                'Heart': 1,
                'Max Heart': 5,
                'Hunger': 3,
                'Max Hunger': 10
            },
            'Skill': {
                'Basic Attack': '10-15'
            }
        }
        display_stats(character)
        actual = mock_output.getvalue()
        expected = 'Basic Attack   : Damage 10-15\n'
        self.assertIn(expected, actual)