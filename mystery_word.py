import random
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

easy_list = []
normal_list = []
hard_list = []


def organize_words():
    print('')
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                if len(word) > 3 and len(word) <= 6:
                    easy_list.append(word)
                elif len(word) > 6 and len(word) <= 8:
                    normal_list.append(word)
                elif len(word) > 8:
                    hard_list.append(word)

def choose_difficulty():
    print("Easy = 4-6 letters, Normal = 6-8 letters, "
          "and Hard is more than 8 letters!")
    difficulty = input("Choose a difficulty! (Easy/Normal/Hard) ").lower()
    if difficulty[0] != "e" and difficulty[0] != "n" and difficulty[0] != "h":
        print("TYPE EASY, NORMAL, OR HARD TO CHOOSE DIFFICULTY")
        main()
    if difficulty[0] == "e":
        rand_word = random.choice(easy_list)
        return rand_word
    elif difficulty[0] == "n":
        rand_word = random.choice(normal_list)
        return rand_word
    elif difficulty[0] == "h":
        rand_word = random.choice(hard_list)
        return rand_word


def user_guess(bad_guesses, good_guesses):
    while len(bad_guesses) < 9:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 0:
            print("You have to guess SOMETHING!")
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


def display(rand_word, good_guesses, bad_guesses, new_guess):
    clear()
    print("\nThe secret word is {} letters long.".format(len(rand_word)))
    if new_guess in rand_word:
        print("\nYour guess was right!")
    elif new_guess not in rand_word:
        print("\nYour guess was wrong!")

    print("You have {} guesses left.".format(8 - len(bad_guesses)))
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
    replay = input("Would you like to play again? (Yes/No) ").lower()
    if replay[0] == 'n':
        exit()
    elif replay[0] == 'y':
        main()
    else:
        exit()


def main():
    good_guesses = []
    bad_guesses = []
    if len(easy_list)<1:
        organize_words()
    rand_word = choose_difficulty()
    while len(bad_guesses) < 9:
        new_guess = user_guess(bad_guesses, good_guesses)
        comparison(new_guess, rand_word, bad_guesses, good_guesses)
        display(rand_word, good_guesses, bad_guesses, new_guess)
        if len(bad_guesses) >= 8:
            loss_condition(rand_word)

if __name__ == "__main__":
    main()
