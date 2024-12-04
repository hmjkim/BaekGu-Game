from unittest import TestCase
from unittest.mock import patch

from minigames.battle import make_enemies


class TestMakeEnemies(TestCase):

    def test_make_enemies_contains_name_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('Name', enemy)

    def test_make_enemies_contains_icon_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')

        self.assertIn('Icon', enemy)

    def test_make_enemies_contains_description_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('Description', enemy)

    def test_make_enemies_contains_level_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('Level', enemy)

    def test_make_enemies_contains_hp_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('HP', enemy)

    def test_make_enemies_contains_basic_attack_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('Basic Attack', enemy['Attack'])

    def test_make_enemies_contains_skill_name_key(self):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        self.assertIn('Hiss', enemy['Attack'])

    @patch('random.randint', return_value=230)
    def test_make_enemies_hp_value_is_within_range(self, _):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        actual = enemy['HP']
        expected = 230
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=150)
    def test_make_enemies_basic_attack_is_within_range(self, _):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        actual = enemy['Attack']['Basic Attack']
        expected = 150
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=350)
    def test_make_enemies_skill_damage_is_within_range(self, _):
        enemy = make_enemies('Guard Cat', '🐱', 'A fierce feline guarding the living room.', '3', (200, 300), (100, 200),
                             (300, 400), 'Hiss')
        actual = enemy['Attack']['Hiss']
        expected = 350
        self.assertEqual(actual, expected)
