import random
import unittest
from mystery_word import *


class TestMysteryWordMethods(unittest.TestCase):
    def test_organize_words(self):
        organize_words()
        self.assertTrue(len(random.choice(easy_list)) <= 6)
        self.assertTrue(len(random.choice(easy_list)) > 3)
        self.assertTrue(len(random.choice(normal_list)) > 6)
        self.assertTrue(len(random.choice(normal_list)) <= 8)
        self.assertTrue(len(random.choice(hard_list)) > 8)

    def test_good_guess(self):
        good_guesses = []
        bad_guesses = []
        new_guess = 'a'
        rand_word = 'apple'
        comparison(new_guess, rand_word, bad_guesses, good_guesses)
        self.assertTrue(len(good_guesses) > 0)
        self.assertTrue(len(bad_guesses) == 0)

    def test_bad_guess(self):
        good_guesses = []
        bad_guesses = []
        new_guess = 'a'
        rand_word = 'blueberry'
        comparison(new_guess, rand_word, bad_guesses, good_guesses)
        self.assertTrue(len(good_guesses) == 0)
        self.assertTrue(len(bad_guesses) > 0)

if __name__ == '__main__':
    unittest.main()
