import random

easy_list = []
medium_list = []
hard_list = []

with open("/usr/share/dict/words", "r") as f:
    for line in f:
        words = line.lower().split()
        for word in words:
            if len(word) > 3 and len(word) < 6:
                easy_list.append(word)
            elif len(word) >= 6 and len(word) <= 8:
                medium_list.append(word)
            else:
                hard_list.append(word)

#def choose_difficulty():
    #user_input = input("Choose a difficulty! (Easy/Medium/Hard) ")
    #return user_input

#def random_word():
#
# def game_start():
#
# def user_guess():
#
# def comparison():
#
# def display():
#
# def repeated_guess():
#
# def win_condition():
#
# def loss_condition():
#
# def game_reset():
print(medium_list)
