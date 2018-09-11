# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:46:11 2017

@author: rosie_000

Exercise 4: Divisors
"""

num = raw_input("Please enter a number: ")
numra = int(num) + 1

x = range(1,numra)

for y in x:
    if int(num) % y == 0:
        print y
        
