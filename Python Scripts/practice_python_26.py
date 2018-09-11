# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:17:56 2017

@author: rosie_000

Exercise 26: Check Tic Tac Toe - given a 3 by 3 list of lists that represents a Tic Tac 
Toe game board, tell me whether anyone has won, and tell me which player won, if any.
"""

matrix = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
print matrix
print matrix[0][0]
print matrix [1][1]
print matrix [2][2]

def ttt_check(game):
    if game[0][1] == game[1][1] == game[2][1] == 1:
        print "Player 1 has won!"
    elif game[0][1] == game[1][1] == game[2][1] == 2:
        print "Player 2 has won!"
    elif game[0][2] == game[1][2] == game[2][2] == 1:
        print "Player 1 has won!"
    elif game[0][2] == game[1][2] == game[2][2] == 2:
        print "Player 2 has won!"
    elif game[0][0] == game[1][0] == game[2][0] == 1:
        print "Player 1 has won!"
    elif game[0][0] == game[1][0] == game[2][0] == 2:
        print "Player 2 has won!"
    elif game[0][0] == game[1][1] == game[2][2] == 1:
        print "Player 1 has won!"
    elif game[0][0] == game[1][1] == game[2][2] == 2:
        print "Player 2 has won!"
    elif game[0][2] == game[1][1] == game[2][0] == 1:
        print "Player 1 has won!"
    elif game[0][2] == game[1][1] == game[2][0] == 2:
        print "Player 2 has won!"
    else:
        for i in game:
            if i[0] == i[1] == i[2] == 1:
                print "Player 1 has won!"
            elif i[0] == i[1] == i[2] == 2:
                print "Player 2 has won!"
        print "No winner."
                

if __name__=="__main__":
    l = [[0, 1, 1],
	[2, 1, 0],
	[2, 1, 2]]
    print ttt_check(l)
    
    
    