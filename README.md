
#HANGMAN

After loading the program, the first user input is going to ask for a difficulty.  Words with lengths 4-6 are considered easy difficulty,
the 6-8 range will be considered normal, and hard difficulty will be even longer.

The difficulty prompt will accept any input that starts with E, N, and H respectively.

After guessing the first letter, the screen will clear and show how long the secret word is, whether or not your guess was in the secret 
word or not, your previous guesses that were wrong, and how many guesses you have left before losing.

The letter guess prompt will accept only single letters, case negligent.  Guessing a letter twice, guessing two letters at a time, or 
any mix of numbers/punctuation will re-prompt the user for single letters.

After either winning (when the accumulated correct guesses amount to the secret word), or losing (after guessing incorrectly 8 times), 
the word will be displayed and the user will be asked if he/she would like to replay the game.  Depending on the input, the game will
either begin again from the beginning or return to the command prompt.


The test file is my feeble attempt at writing my own suite of unittests and will hopefully be amended once I learn how to incorporate 
testing into my programs.
