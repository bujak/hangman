"""
HangMan Game
Diana Tokarska
Tomasz Bujakowski
Codecool 2016, Kraków
"""

####### IMPORTANT #######
#
#   Put capitals.txt in the same folder as hangman.py
#   to avoid errors with importing names.
#
#########################

import random
import sys
import os

# welcoming text
os.system('clear')
print('\033[93m' + 'Evil ' + '\033[91m' + 'SKYNET' + '\033[93m' + ''' is trying to take control over the world.
Guess a names of European capital that are his targets and safe the world!\n''' + '\033[0m')


# creating empty lists which will be used later
capitals = []
cap_name_output = []
not_in_word = []
lifes = 5

# importing capital cities from file and storing them in list
with open("capitals.txt", "r") as capital:
    for item in capital:
        capitals.append(item.replace('\n', ''))
    capital.close()
cap_name = list(random.choice(capitals))


# filling another list with dashes and * if there is a space
for letter in cap_name:
    for n, i in enumerate(cap_name):
        if i == ' ':
            cap_name[n] = '*'
    if letter == '*':
        cap_name_output.append('*')
    else:
        cap_name_output.append('_ ')


# print(cap_name) #cheat mode


# chcecking player's lifes, close program when lifes reaches 0
def zero_lifes(lifes):
    if lifes == 0:
        print('\033[91m' + 'GAME OVER!' + '\033[0m')
        sys.exit()


# checking typed word
def word(type_word, lifes):
    #user can type space for guessing and it will changed by script for matching with capital name
    if ' ' in type_word:
        for n, i in enumerate(type_word):
            if i == ' ':
                type_word[n] = '*'

    if type_word == cap_name:
        print('\033[92m' + 'YOU WON!' + '\033[0m')
        sys.exit()
    else:
        game(lifes - 1)


#checks if letter is in cap. name, it not, letter is added to list
def wrong_letter(type_letter, not_in_word, lifes):
    not_in_word.append(type_letter)
    print("\nUsed letters: " + ', '.join(not_in_word))
    game(lifes - 1)

# main game function
def game(lifes):
    print('You have', lifes, ' lifes.')
    print('\033[1m' + ''.join(cap_name_output) + '\033[0m' + '\n')

    zero_lifes(lifes)

    choice = input('Would You like to guess a letter or whole word(s)? ').lower()

    if choice == 'letter' or choice == 'l':

        #list with used letters is shown when is not empty
        if not_in_word != []:
            print("Used letters: " + ', '.join(not_in_word))

        #checking user input if it is letter or space
        if '_ ' in cap_name_output:
            type_letter = input('Type letter: ').upper()
            while not len(type_letter) == 1:
                print('You can type only letters and spaces. Try again.')
                type_letter = input('Type letter: ').upper()
            while not type_letter.isalpha():
                print('You can type only letters and spaces. Try again.')
                type_letter = input('Type letter: ').upper()

            if type_letter not in cap_name:
                wrong_letter(type_letter, not_in_word, lifes)

            #script check every letter in capital and change signs is appropriate for typed letter
            for letter, i in enumerate(cap_name):
                if i == type_letter:
                    cap_name_output[letter] = type_letter
            #print(''.join(cap_name_output))

            #if every dash is changed for letter player wins
            if '_ ' not in cap_name_output:
                print('\033[92m' + 'YOU WON!' + '\033[0m')
                sys.exit()
            game(lifes)


    #this block will run if player want to type word
    elif choice == 'word' or choice == 'w':
        type_word = list(input('Type word: ').upper())
        word(type_word, lifes)


    else:
        print('You can chose only between letter or word, type again!')
        game(lifes)


# user can change difficulty level, to determine number of lifes
def levels():
    input_level = input('Do you chose EASY, MEDIUM or HARD level? ').lower()
    if input_level == 'easy':
        game(15)
    elif input_level == 'medium':
        game(10)
    elif input_level == 'hard':
        game(5)
    else:
        print('There no such level, type again!')
        levels()


# intro for game
def start_game():
    start = input('Do sure you want start the game and save The World? There will be no return...(enter "yes" to continue) ').lower()
    if start == 'yes' or start == 'y':
        levels()
    else:
        sys.exit()

# calling funtions

start_game()

game(5)
