from unittest import TestCase
from minigames.hangman import lists_of_words


class Test(TestCase):
    def test_lists_of_words_letters_4(self):
        words = lists_of_words()
        actual = words[0]
        expected = ["book", "tree", "blue", "love", "care", "hope", "door", "jump", "play", "work", "fish", "swim",
                    "ball", "hand", "cake", "sing", "walk", "rain", "star", "wind", "read", "rock", "band", "ship",
                    "moon", "face", "line", "ride", "time", "life"]
        self.assertEqual(actual, expected)

    def test_lists_of_words_letters_6(self):
        words = lists_of_words()
        actual = words[2]
        expected = ["garden", "silver", "branch", "butter", "turtle", "bridge", "rabbit", "pebble", "button", "stream",
                    "travel", "bottle", "winter", "flower", "basket", "orange", "desert", "magnet", "planet", "frozen",
                    "safety", "forest", "guitar", "friend", "yellow", "ticket", "pencil", "bridge", "jungle", "school"]
        self.assertEqual(actual, expected)


