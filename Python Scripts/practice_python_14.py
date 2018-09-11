# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:00:25 2017

@author: rosie_000

Exercise 14: Write a function that takes list, removes the duplicates and returns a new list
"""
import random

def dup_remove(alis):
    newlist = []
    for i in alis:
        if i not in newlist:
           newlist.append(i)
    print newlist

a = [1,1,5,6,4,3,2,5,7,0,9,7]

dup_remove(a)

"""Extra 1: Write the function using a set"""
        
def dup_remove2(blis):
    blis = set(blis)
    blis=list(blis)
    print blis
    
b = [1,2,3,2,5,7,4,9,1,4,5]

dup_remove2(b)

"""Extra 2: Do Exercise 5 (take two lists and return one with shared elements) using sets"""

"""def dup_remove3(clis):
    dlis = random.sample(range(50),10)"""
    
    