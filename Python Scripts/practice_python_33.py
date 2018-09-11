# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:35:04 2018

@author: rosie_000

Exercise 33: Birthday Dictionary
For this exercise, we will keep track of when our friend’s birthdays are, and be able 
to find that information based on their name. Create a dictionary (in your file) of 
names and birthdays.
"""
birthday_dictionary = {"Mum": "6th April",
"Dad":"26th May",
"Jamie":"10th October",
"Charlotte":"16th April",
"Priya":"9th February",
"Kelsey":"29th February",}

birthday_dictionary["Eloise"] = "16th December"

print(birthday_dictionary.keys())

if "Dad" in birthday_dictionary:
    print "Yay"


if __name__ == '__main__':
    print ("Welcome to the birthday dictionary! We know the birthdays of: ")
    for key in birthday_dictionary:
        print ("\n"+key)
    name = raw_input("Please enter a name to be searched: ")
    if name in birthday_dictionary:
        print("{}'s birthday is on {}.".format(name,birthday_dictionary[name]))
    else:
        print("I'm sorry, we don't have {} in our database.".format(name))