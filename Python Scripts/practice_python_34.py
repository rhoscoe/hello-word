# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:11:50 2018

@author: rosie

Exercise 34: In this exercise, modify your program from Part 1 to load the birthday 
dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
"""

import json

birthday_dictionary = {"mum": "6th April",#make a dict
"dad":"26th May",
"jamie":"10th October",
"charlotte":"16th April",
"priya":"9th February",
"kelsey":"29th February",}

with open("bday.json", "w") as f:
    json.dump(birthday_dictionary, f) #create json containing the dict above
    
with open("bday.json", "r") as f: #open/load the json
    bday = json.load(f)

if __name__ == '__main__':
    print ("Welcome to the birthday dictionary! We know the birthdays of: ")
    for key in bday:
        print ("\n"+key)
    name = raw_input("Please enter a name to be searched: ")
    if name in bday:
        print("{}'s birthday is on {}.".format(name,bday[name]))
    else:
        print("I'm sorry, we don't have {} in our database.".format(name))
    addname = raw_input("Would you like to add another birthday? Type 'y' if you'd like to do so ")
    if addname == 'y':
        nname = raw_input("Please write their name: ")
        nbday = raw_input("Please write the date and month of their birthday eg. 1st January: ")
        bday[nname] = nbday
        with open("bday.json", "w") as f:
            json.dump(bday, f)
        
   #
        
"""Bonus - Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name. """