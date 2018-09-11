# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:33:41 2017

@author: rosie_000

Exercise 23: Given two .txt files that have lists of numbers in them, find the numbers that
 are overlapping. One .txt file has a list of all prime numbers under 1000, and the other
 .txt file has a list of happy numbers up to 1000.
"""

primes = []

with open('exercise_23_primes.txt', 'r') as of:
    line = of.readline()
    while line:
        primes.append(int(line.strip()))
        line = of.readline()
        
happy = []

with open('exercise_23_happy.txt', 'r') as of:    
    line = of.readline()
    while line:
        happy.append(int(line.strip()))
        line = of.readline()

overlap = []

for i in primes:
    if i in happy:
        overlap.append(i)

print overlap

"""Using a function and list comprehension"""
def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('exercise_23_primes.txt')
happieslist = filetolistofints('exercise_23_happy.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)


    