# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 11:02:02 2017

@author: rosie_000

Exercise 10: Write a program that takes a list and makes a new list of the first and last numbers
"""

import random

def alpha_omega(a):
    print(a)
    emp = []
    emp.append(a[0])
    emp.append(a[-1])
    print(emp)

lis = random.sample(range(50),8)

alpha_omega(lis)

def al_om(x):
    print(x)
    print([x[y] for y in [0,-1]])

li = random.sample(range(50),8)

al_om(li)