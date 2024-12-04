from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from minigames.battle import display_enemy_info


class TestDisplayEnemyInfo(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_information(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        expected_output = "------------------------------------------------------\n" \
                          "‼️‼️ ENEMY ENCOUNTERED ‼️‼️\n" \
                          "------------------------------------------------------\n" \
                          "🐭 Mouse\n" \
                          "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!\n" \
                          "Level: 1\n" \
                          "HP: 90/90\n" \
                          "------------------------------------------------------\n\n"
        self.assertEqual(print_result, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_name(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        self.assertIn('Mouse', print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_icon(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        self.assertIn('🐭', print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_level(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        self.assertIn('Level: 1', print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_description(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        self.assertIn("A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                      print_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_enemy_info_shows_correct_HP(self, mock_output):
        enemy = {'Name': 'Mouse', 'Icon': '🐭',
                 'Description': "A tiny mouse nibbling on a piece of cheese. It looks harmless, but don't let your guard down!",
                 'Level': '1', 'HP': 90, 'Attack': {'Nibble': 13, 'Basic Attack': 8}}
        display_enemy_info(enemy)
        print_result = mock_output.getvalue()
        self.assertIn('HP: 90/90', print_result)
