# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:36:30 2017

@author: rosie_000

Exercise 5: List Overlap
"""
import random

a = [1,2,2,3,6,13,19,20,25,38,41,52]
b = [1,5,8,19,25,37,41,90]
c=[]

for elem in a:
    if elem in b:
        c.append(elem)
print(c)

"""Extra 1: do this with randomly generated lists"""

ara = random.sample(range(50),10)
bra = random.sample(range(50),10)

cra = [0]

for elem in ara:
    if elem in bra:
        cra.append(elem)
print(cra)

"""Extra 2: Write the first activity in one line"""

