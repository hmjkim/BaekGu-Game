from unittest import TestCase
from hangman import check_character_level_hangman, lists_of_words


class Test(TestCase):
    def test_check_character_level_hangman_level_1(self):
        character = {'Stat': {'Level': 1}}
        lists = lists_of_words()
        actual = check_character_level_hangman(character, lists)
        expected = ["garden", "silver", "branch", "butter", "turtle", "bridge", "rabbit", "pebble", "button", "stream",
                    "travel", "bottle", "winter", "flower", "basket", "orange", "desert", "magnet", "planet", "frozen",
                    "safety", "forest", "guitar", "friend", "yellow", "ticket", "pencil", "bridge", "jungle", "school"]
        self.assertEqual(actual, expected)

    def test_check_character_level_hangman_level_3(self):
        character = {'Stat': {'Level': 3}}
        lists = lists_of_words()
        actual = check_character_level_hangman(character, lists)
        expected = ["book", "tree", "blue", "love", "care", "hope", "door", "jump", "play", "work", "fish", "swim",
                    "ball", "hand", "cake", "sing", "walk", "rain", "star", "wind", "read", "rock", "band", "ship",
                    "moon", "face", "line", "ride", "time", "life"]
        self.assertEqual(actual, expected)
