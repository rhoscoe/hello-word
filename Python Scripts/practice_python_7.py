# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:22:27 2017

@author: rosie_000

Exercise 7: List Comprehension
"""
import random

bra = random.sample(range(50),10)
print bra

print([i for i in bra if int(i)%2 ==0])