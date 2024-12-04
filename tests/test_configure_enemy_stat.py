from unittest import TestCase

from minigames.battle import configure_enemy_stat


class TestConfigureEnemyStat(TestCase):

    def test_configure_enemy_stat_contains_hp_range_key(self):
        enemy_stat = configure_enemy_stat()
        self.assertIn('HP Range', enemy_stat)

    def test_configure_enemy_stat_contains_basic_attack_key(self):
        enemy_stat = configure_enemy_stat()
        self.assertIn('Basic Attack', enemy_stat)

    def test_configure_enemy_stat_contains_skill_damage_key(self):
        enemy_stat = configure_enemy_stat()
        self.assertIn('Skill Damage', enemy_stat)

    def test_configure_enemy_stat_hp_range_level_1_value_is_80_100(self):
        enemy_stat = configure_enemy_stat()
        actual = enemy_stat['HP Range']['Level 1']
        expected = (80, 100)
        self.assertEqual(actual, expected)

    def test_configure_enemy_stat_basic_attack_level_1_value_is_5_10(self):
        enemy_stat = configure_enemy_stat()
        actual = enemy_stat['Basic Attack']['Level 1']
        expected = (5, 10)
        self.assertEqual(actual, expected)

    def test_configure_enemy_stat_skill_damage_level_1_value_is_10_25(self):
        enemy_stat = configure_enemy_stat()
        actual = enemy_stat['Skill Damage']['Level 1']
        expected = (10, 25)
        self.assertEqual(actual, expected)
