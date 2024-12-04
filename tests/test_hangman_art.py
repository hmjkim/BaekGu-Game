from unittest import TestCase
from minigames.hangman_art import stage


class Test(TestCase):
    def test_stage_whole_stage(self):
        expected = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''', '''
          +---+
              |
              |
              |
              |
              |
        =========
        ''', '''
              +
              |
              |
              |
              |
              |
        =========
        ''']

        actual = stage()
        self.assertEqual(actual, expected)
