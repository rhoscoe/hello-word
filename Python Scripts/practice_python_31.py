# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:13:27 2018

@author: rosie_000
Exercise 31: Guess Letters
write the logic that asks a player to guess a letter and displays letters in the clue word
 that were guessed correctly. For now, let the player guess an infinite number of times 
 until they get the entire word.
"""

guesses = []

"""def guess_lets(word):
    word = list(word)
    print "Welcome to Hangman!"
    guessed = ("_ "*len(word))
    print guessed
    guessed = list(guessed)
    gu = raw_input("Guess a letter: ")
    gu = gu.lower
    while True:
        if gu in guesses:
            print "Already guessed!"
        else:
            guesses.append(gu)
        if gu in word:
            ind = word.index(gu)
            guessed[ind] = gu
            word[ind] = '_'
        else:
             gu = raw_input("Guess a letter: ")
             gu = gu.lower 
        if '_' not in word:
            print('You won!')
            break
            
            

guess_lets('hello')"""

if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = "EVAPORATE"
	guessed = "_" * len(word)
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
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
			break
    