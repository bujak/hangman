"""
HangMan Game
Diana Tokarska
Tomasz Bujakowski
Codecool 2016, Kraków
"""

####### IMPORTANT #######
#
#   Put capitals.txt in the same folder as main file
#   to avoid errors with importing names.
#
#########################

import random
import sys
import os

class HangMan:

    def __init__(self):
        self.capitals = []
        self.cap_name_output = []
        self.not_in_word = []
        self.cap_name = []
        self.choice = ' '
        self.type_letter = ' '
        self.type_word = ' '


    # importing capital cities from file, storing them in list,
    # choosing one of them radomly
    def make_capitals(self):
        with open("capitals.txt", "r") as capital:
            for item in capital:
                self.capitals.append(item.replace('\n', ''))
            capital.close()
        self.cap_name = list(random.choice(self.capitals))


    # filling another list with dashes and * if there is a space
    def make_dashes(self):
        for letter in self.cap_name:
            for n, i in enumerate(self.cap_name):
                if i == ' ':
                    self.cap_name[n] = '*'
            if letter == '*':
                self.cap_name_output.append('*')
            else:
                self.cap_name_output.append('_ ')


    # chcecking player's lifes, close program when lifes reache
    def end_game(self,lifes):
        if lifes == 0:
            print('\033[91m' + 'GAME OVER!' + '\033[0m')
            sys.exit()


    #checking user input if it is letter or space
    def check_letter(self):
        while not len(self.type_letter) == 1:
            print('You can type only letters and spaces. Try again.')
            self.type_letter = input('Type letter: ').upper()
        while not self.type_letter.isalpha():
            print('You can type only letters and spaces. Try again.')
            self.type_letter = input('Type letter: ').upper()

    # checking input if it is in capital name, changes dash for input letter in list
    # if there is no dashes in list, player win
    def letter(self,lifes):
        if self.not_in_word != []:
            print("Used letters: " + ', '.join(self.not_in_word))
        if '_ ' in self.cap_name_output:
            self.type_letter = input('Type letter: ').upper()
            self.check_letter()
            if self.type_letter not in self.cap_name:
                self.not_in_word.append(self.type_letter)
                print('\n' + '\033[1m' + ''.join(self.cap_name_output) + '\033[0m' + '\n')
                self.game(lifes - 1)
            for letter, i in enumerate(self.cap_name):
                if i == self.type_letter:
                    self.cap_name_output[letter] = self.type_letter
            print('\n' + '\033[1m' + ''.join(self.cap_name_output) + '\033[0m' + '\n')
            if '_ ' not in self.cap_name_output:
                print('\033[92m' + 'YOU WON!' + '\033[0m')
                sys.exit()
            self.game(lifes)


    # checking if in entered word(s) is space and changing spaces for *
    # comparing typed word with capital name
    def word(self,lifes):
        self.type_word = list(input('Type word: ').upper())
        if ' ' in self.type_word:
            for n, i in enumerate(self.type_word):
                if i == ' ':
                    self.type_word[n] = '*'
        if self.type_word == self.cap_name:
            print('\033[92m' + 'YOU WON!' + '\033[0m')
            sys.exit()
        else:
            self.game(lifes - 1)


    # asking user for input, runs appropriate function depending on input
    def game(self,lifes):
        print('\nYou have', lifes, ' lifes.')
        self.end_game(lifes)
        self.choice = input('Would You like to guess a letter or whole word(s)? ').lower()
        if self.choice == 'letter' or self.choice == 'l':
            self.letter(lifes)
        elif self.choice == 'word' or self.choice == 'w':
            print('\033[1m' + ''.join(self.cap_name_output) + '\033[0m' + '\n')
            self.word(lifes)
        else:
            print('You can chose only between letter or word, type again!')
            self.game(lifes)


    # user can set difficulty level, to determine number of lifes
    def levels(self):
        input_level = input('Do you chose EASY, MEDIUM or HARD level? ').lower()
        print('\n' + '\033[1m' + ''.join(self.cap_name_output) + '\033[0m' + '\n')
        if input_level == 'easy' or input_level == 'e':
            self.game(15)
        elif input_level == 'medium' or input_level == 'm':
            self.game(10)
        elif input_level == 'hard' or input_level == 'h':
            self.game(5)
        else:
            print('There no such level, type again!')
            self.levels()

    # star game function
    def start_game(self):
        start = input('Do sure you want start the game and save The World? There will be no return...(enter "yes" to continue) ').lower()
        if start == 'yes' or start == 'y':
            self.levels()
        else:
            sys.exit()

    def main(self):
        os.system('clear')
        print('\033[93m' + 'Evil ' + '\033[91m' + 'SKYNET' + '\033[93m' + ''' is trying to take control over the world.
        Guess a names of European capital that are his targets and safe the world!\n''' + '\033[0m')
        self.make_capitals()
        self.make_dashes()
        self.start_game()
        self.levels

new_game = HangMan()
new_game.main()
