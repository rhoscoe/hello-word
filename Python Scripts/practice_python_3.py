# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:59:24 2017

@author: rosie_000
"""

a = [1,2,3,4,5,6,7,8,9,10]

for x in a:
    if x <= 5:
        print(x)
        
"""extra 1: print the elements out in their own list"""

b = [1,2,3,7,9,42]
c = []

for x in b:
    if x <= 5:
        c.append(x)
print(c)

"""extra 2: write in one line"""

print([i for i in [1,2,4,6,8,11] if i<=5])

"""extra 3: ask user for a number, and return a list with elements smaller than the user's number"""

d = [2,3,5,7,8]
e = []

us = raw_input("Please enter a number: ")

for x in d:
    if x <= int(us):
        e.append(x)
print(e)