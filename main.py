#Step 1 
from random import randint
from hangman_words import word_list


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





blanck = []

from hangman_art import logo
print(logo)

#-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
for word in word_list:
  chosen_word = word_list[randint(0, (len(word)-1))]

word_leght = len(chosen_word)
blanck = [" _ "] * word_leght
count = 0
lives = len(HANGMANPICS)
guessed_letter = []
guessed_list = ""
guessed = ""
#-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while lives > 0:
    print(''.join(blanck))
    print("\n########################################\n")
    guess = input("Guess a letter: ").lower()
    print("\n########################################\n")



#T-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # for letter in chosen_word:

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            blanck[i] = guess
            guessed = ''.join(blanck)





    if guess not in chosen_word:
        lives -= 1
        print (f""" 

         {HANGMANPICS[count]}

""")
        print(f"\nIncorrect guess. Lives left: {lives}\n")
        count += 1
        guessed_letter.append(guess)
        guessed_list = ''.join(guessed_letter)
        print("\n########################################\n")
        print(f"\nList of wrong guesses:  {guessed_list}\n")

    print("\n########################################\n")
    print (f" \nYour word looks like this: {guessed}\n ") 
    print("\n########################################\n")

    if " _ " not in blanck:
            print("\n########################################\n")
            print("\nCongratulations! You guessed the word.\n")
            print("\n########################################\n")
            break

    if not lives:
        print("\n########################################\n")
        print(f"\nSorry, you ran out of lives. The correct word was '{chosen_word}'.")
        print("\n########################################\n")