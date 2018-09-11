# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 20:15:22 2017

@author: rosie_000

Exercise 10: Write a program that lists the duplicates in two lists using list comprehension
"""
import random 

a = [3,4,6,8,15,19,23,25,32]
b = [5,8,15,21,25,27,30]

print([x for x in a if x in b])

"""Extra: Use randomly generates lists"""

print([x for x in random.sample(range(50),10) if x in random.sample(range(50),8)])