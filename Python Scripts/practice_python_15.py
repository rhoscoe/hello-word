# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:04:28 2017

@author: rosie_000

Exercise 14: Ask the user for a sentence, then reverse the sentence and return it
"""

def reverse(sen):
    words = sen.split()
    rev = words[::-1]
    fin = " ".join(rev)
    print fin

reverse(raw_input("Write a sentence: "))