# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:51:15 2017

@author: rosie_000

Implement a function that takes as input three variables, and returns the largest of the 
three. Do this without using the Python max() function!
"""

def biggest(a,b,c):
    if a > b and a > c:
        return a
        print a
    elif b > a and b > c:
        return b
        print b
    elif c > a and c > b:
        return c
        print c

print biggest(7,100,83)