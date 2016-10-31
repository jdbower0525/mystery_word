import unittest
from mystery_word import random_word
from mystery_word import game_reset
from mystery_word import loss_condition



class TestMysteryWordFunctions(unittest.TestCase):

    def test_game_reset(self):
        user_input_1 = False
        self.assertRaises(SystemExit, user_input_1)
        user_input_2 = True
        self.assertEqual(main(), user_input_2)

    def test_loss_condition(self):
        self.return_value = "random"
        self.side_effect = list("bcdefgh")
        mystery_word.main()
        self.xprint.assert_any_call("The secret word was random")

    def test_random_word(self):
       user_diff_choice_one = 'e'
       user_diff_choice_two = 'm'
       user_diff_choice_three = 'h'
       easy = ['easy']
       medium = ['mediums']
       hard = ['difficults']
       random_word_one = random_word()
       random_word_two = random_word()
       random_word_three = random_word(user_diff_choice_three, easy, medium, hard)
       self.assertEqual(random_word_one, 'easy')
       self.assertEqual(random_word_two, 'mediums')
       self.assertEqual(random_word_three, 'difficults')

if __name__ == '__main__':
    unittest.main()
