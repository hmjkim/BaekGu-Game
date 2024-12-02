from unittest import TestCase
from hangman import word_strike


class Test(TestCase):
    def test_word_strike_1_word(self):
        word = 'p'
        actual = word_strike(word)
        expected = '̶p'
        self.assertEqual(actual, expected)

    def test_word_strike_3_word(self):
        word = 'dog'
        actual = word_strike(word)
        expected = '̶d ̶o ̶g'
        self.assertEqual(actual, expected)

    def test_word_strike_6_word(self):
        word = 'python'
        actual = word_strike(word)
        expected = '̶p ̶y ̶t ̶h ̶o ̶n'
        self.assertEqual(actual, expected)

    def test_word_strike_punctuation(self):
        word = '!'
        actual = word_strike(word)
        expected = '̶!'
        self.assertEqual(actual, expected)

    def test_word_strike_mixed_punctuation(self):
        word = 'dog!'
        actual = word_strike(word)
        expected = '̶d ̶o ̶g ̶!'
        self.assertEqual(actual, expected)

    def test_word_strike_mixed_number(self):
        word = 'dog!123'
        actual = word_strike(word)
        expected = '̶d ̶o ̶g ̶! ̶1 ̶2 ̶3'
        self.assertEqual(actual, expected)







