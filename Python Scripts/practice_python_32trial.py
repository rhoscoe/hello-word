# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 19:52:48 2018

@author: rosie_000
"""
"""import random

def get_word(): #chooses a random word from the text file
    with open('sowpods.txt', 'r') as f:
        text = list(f)
        word =  random.choice(text).strip()
        word = list(word)
        return word"""

"""def get_letter(): #asks the user for a letter, strips it and capitalises it
    letter = raw_input("Guess a letter: ")
    return letter.strip().upper()"""

"""if __name__ == '__main__':
    word = get_word()
    print word
    #call random word word
    display = '_'*len(word)#underscores the same length as the  word
    ldisplay = list(display)
    already = [] #empty list for guessed letters to go in
    count = 6 #counts the number of goes
    while count > 1:
        letter = raw_input("Guess a letter: ")
        letter = letter.strip().upper()
        if letter in already:
            print "You guessed that already! Try again"
        else:
            already.append(letter)
            for i in range(0,len(word)-1):
                if word[i] == letter:
                    ldisplay[i] = letter
                    word[i] == '_'
                else: #you're doing this for every letter in the word that ISN'T the guessed word
                    count-=1
                    print("Try again. You have "+str(count)+" goes.")
        if '_' not in ldisplay:
            print "Congratulations, you guessed the word!" """


