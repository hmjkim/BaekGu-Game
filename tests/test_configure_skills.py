from unittest import TestCase
from unittest.mock import patch

from game import configure_skills


class TestConfigureSkills(TestCase):

    def test_configure_skills_contains_level_1_key(self):
        enemy_stat = configure_skills()
        self.assertIn('Level 1', enemy_stat)

    def test_configure_skills_contains_level_2_key(self):
        enemy_stat = configure_skills()
        self.assertIn('Level 2', enemy_stat)

    def test_configure_skills_contains_level_3_key(self):
        enemy_stat = configure_skills()
        self.assertIn('Level 3', enemy_stat)

    def test_configure_skills_contains_skill_has_damage_key(self):
        enemy_stat = configure_skills()
        self.assertIn('Damage', enemy_stat['Level 1']['Bark'])

    def test_configure_skills_contains_skill_has_description_key(self):
        enemy_stat = configure_skills()
        self.assertIn('Description', enemy_stat['Level 1']['Bark'])

    @patch('random.randint', return_value=24)
    def test_configure_skills_level_1_skill_damage_is_within_range(self, _):
        enemy_stat = configure_skills()
        actual = enemy_stat['Level 1']['Bark']['Damage']
        expected = 24
        self.assertEqual(actual, expected)

    def test_configure_skills_level_1_skill_has_correct_description(self):
        enemy_stat = configure_skills()
        actual = enemy_stat['Level 1']['Bark']['Description']
        expected = 'A loud bark that stuns the enemy'
        self.assertEqual(actual, expected)
