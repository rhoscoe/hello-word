# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 11:37:48 2017

@author: rosie_000

Exercise 24: Ask the user what size game board they want to draw, and draw it for them 
to the screen using Python’s print statement.
"""

def gameboard(r = input("How many rows? "),c = input("How many columns? ")):
    r = int(r)+1 #how many rows of dashes (r+1)
    c = int(c) #how many | (c+1), how many sets of dashes (c)
    while r>0:
        if r>1:
            print " --- "*c
            print "|   |"*c
            r -=1
        elif r == 1:
            print " --- "*c
            r -=1
        """if r > 1:
            print " --- "*c
            print "|   |"*c
            r -=1
        elif r == 0:
            print lastrow*c
            r -=1"""
        
if __name__ == "__main__":
     print "Let's make a gameboard!"
     gameboard()
     
"""r = 3
c = 3

while r>0:
    if r>1:
        print " --- "*c
        print "|   |"*c
        r -=1
        print r
    elif r == 1:
        print " --- "*c
        r -=1
        print r"""


    

    
    
    
    

