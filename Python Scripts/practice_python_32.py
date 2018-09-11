# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 10:52:48 2018

@author: rosie_000

Exercise 32: Hangman
In this exercise, we will finish building Hangman. In the game of Hangman, the player 
only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already 
guessed, don’t penalize them - let them guess again.
"""

import random

def get_word():
    with open('sowpods.txt', 'r') as f:
        text = list(f)
        word =  random.choice(text).strip()
        word = list(word)
        return word

"""def game_setup():
    word = get_word
    guessed = "_"*len(word)
    guessed = list(guessed)


def hangmancheck(line):
    if '_' not in line:
        print("You won!")"""

if __name__ == '__main__':
    print("Welcome to hangman!!")
    word = get_word()
    print word
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    count = 6
    letter = raw_input("Guess a letter: ")
    while count>0 and letter!= "exit":
        print(''.join(guessed))
        if letter.upper() in lstGuessed:
            print("Already guessed!!")
        else:
            for i in range(0,len(word)-1):
                if word[i]==letter.upper():
                    guessed[i] = letter.upper()
                    word[i] = '_'
                else:
                    count-=1
                    print("You have "+str(count)+" goes left.")
                    letter = raw_input("guess letter: ")
                lstGuessed.append(letter.upper())
        if '_' not in guessed:
		print("You won!!")
		break

"""problems 
- printing the line every time it goes through the loop, which can be a
bunch of times
- count goes on to long
- a go is taken even when you get the right letter (letters iterate again until their
already guessed)
- a go is taken when you've already made that guess"""

"""print("Welcome to hangman!!")
word = "EVAPORATE"
guessed = "_" * len(word)
word = list(word)
guessed = list(guessed)
lstGuessed = set()
letter = raw_input("guess letter: ")
while True:
		if letter.upper() in lstGuessed:
			letter = ''
			print("Already guessed!!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter is not '':
				lstGuessed.append(letter.upper())
			letter = raw_input("guess letter: ")
		if '_' not in guessed:
			print("You won!!")
			break"""