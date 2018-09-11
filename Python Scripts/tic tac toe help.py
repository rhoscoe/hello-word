# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 10:23:49 2017

@author: rosie_000
"""

def floo(x):
    if x == 2:
        win = 1
        return win
    

if __name__ == '__main__':
    x = [1,3,4,6,2]    
    c = 10
    win = floo(x)
    while c>0:
        floo(x)
        for i in x:
            if win == 1:
                print "Win!"
                break
            else:
                c-=1
            if c == 0:
                print "Finish!"
                break