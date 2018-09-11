# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 10:59:56 2018

@author: rosie_000

Exercise 30: Pick Word
Write a function that picks a random word from a list of words from the SOWPODS dictionary.
"""

import random



with open('sowpods.txt', 'r') as f:
    text = list(f)
    print (random.choice(text).strip())

#alternatively, could create an empty list, append each line to the list, then select
#a random element use radint