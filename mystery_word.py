import random
import sys
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def random_word():
    easy_list = []
    normal_list = []
    hard_list = []
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                if len(word) > 3 and len(word) <= 6:
                    easy_list.append(word)
                elif len(word) >= 6 and len(word) <= 8:
                    normal_list.append(word)
                elif len(word) > 8:
                    hard_list.append(word)
    difficulty = input("Choose a difficulty! (Easy/Normal/Hard) ").lower()
    if difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
        print("TYPE EASY, NORMAL, OR HARD TO CHOOSE DIFFICULTY")
        main()
    if difficulty == "easy":
        rand_word = random.choice(easy_list)
        return rand_word
    elif difficulty == "normal":
        rand_word = random.choice(normal_list)
        return rand_word
    elif difficulty == "hard":
        rand_word = random.choice(hard_list)
        return rand_word

# def game_start():
#
def user_guess(bad_guesses, good_guesses):
    while len(bad_guesses) < 9:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 0:
            print("Guess something idiot...")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        elif len(guess) != 1:
            print("Guess ONE letter!")
            continue
        return guess

def comparison(new_guess, rand_word, bad_guesses, good_guesses):
    if new_guess in rand_word:
        good_guesses.append(new_guess)
        return good_guesses
    elif new_guess not in rand_word:
        bad_guesses.append(new_guess)
        return bad_guesses

def display(rand_word, good_guesses, bad_guesses):
    clear()
    print("\nYou have {} guesses left.".format(8 - len(bad_guesses)))
    print("Your misses so far have been: \n{}".format(bad_guesses))
    empty_list = []
    for letter in rand_word:
        if letter in good_guesses:
            print(letter, end=' ')
            empty_list.append(letter)
        else:
            print('_', end=' ')

    print(" ")
    for letter in rand_word:
        remaining_letters = (len(rand_word)-len(empty_list))
    if remaining_letters == 0:
        win_condition(rand_word, bad_guesses)

def win_condition(rand_word, bad_guesses):
    clear()
    print("\nCONGRATULATIONS!!! The secret word was {}.".format(rand_word))
    print("You only guessed wrong {} times!".format(len(bad_guesses)))
    game_reset()

def loss_condition(rand_word):
    clear()
    print("\nOH NO! You ran out of guesses!")
    print("The secret word was {}.".format(rand_word))
    game_reset()

def game_reset():
    replay = input("Would you like to play again? (Yes/No) ")
    if replay == 'no':
        exit()
    elif replay == 'yes':
        main()
    else:
        exit()

def main():
    good_guesses = []
    bad_guesses = []
    rand_word = random_word()
    while len(bad_guesses) < 9:
        new_guess = user_guess(bad_guesses, good_guesses)
        comparison(new_guess, rand_word, bad_guesses, good_guesses)
        display(rand_word, good_guesses, bad_guesses)
        if len(bad_guesses) >= 8:
            loss_condition(rand_word)
main()
