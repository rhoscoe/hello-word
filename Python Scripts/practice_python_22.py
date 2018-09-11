# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:44:29 2017

@author: rosie_000

Exercise 22: Given a .txt file that has a list of a bunch of names, count how many of each
 name there are in the file, and print out the results to the screen.
"""

counting_names = {}

with open('names.txt', 'r') as of:
    line = of.readline()
    while line:
        line = line.strip()#get rid of white space
        if line in counting_names:
            counting_names[line]+=1
        else:
            counting_names[line]=1#first time line = Lea (the value, its key will become 1)
        line = of.readline()

print counting_names

"""Extra: take a different text file, and count how many of each “category” of each image there
 are. This text file is actually a list of files corresponding to the SUN database scene 
 recognition database, and lists the file directory hierarchy for the images."""
 
category = {}
 
with open('Exercise_22_extra.txt', 'r') as of:
    line = of.readline() 
    while line:
        line = line.strip()#get rid of white space
        line = line[3:-25]#this part contains the category info of the string
        if line in category:
            category[line]+=1
        else:
            category[line]=1#first time line = abbey (the value, its key will become 1)
        line = of.readline()

print category