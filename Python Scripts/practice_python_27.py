# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 11:40:20 2017

@author: rosie_000

Exercise 27: Tic Tac Toe Draw - When a player (say player 1, who is X) wants to place 
an X on the screen, they can’t just click on a terminal. So we are going to approximate 
this clicking simply by asking the user for a coordinate of where they want to place their
 piece.
"""

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

play1 = "1,3"
 
list = play1.split(",")
x = int(list[0])
y = x - 1



def tictactoe(game):
    x = 9
    while x > 0:
        if x%2 != 0:
            play1 = raw_input("Player 1, please enter your move in the format: row, col: ")
            play1_list = play1.split(",")
            row1 = int(play1_list[0]) - 1
            col1 = int(play1_list[1]) - 1
            if game[row1][col1] == 0:
                game[row1][col1] = "X"
                print game
                x-=1
            else:
                print "Square already used, please try again!"
        if x%2 == 0:
            play2 = raw_input("Player 2, please enter your move in the format: row, col: ")
            play2_list = play2.split(",")
            row2 = int(play2_list[0]) - 1
            col2 = int(play2_list[1]) - 1
            if game[row2][col2] == 0:
                game[row2][col2] = "O"
                print game
                x-=1
            else:
                print "Square already used, please try again!"

if __name__=="__main__":
    game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
    print tictactoe(game)