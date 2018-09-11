# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 11:08:43 2017

@author: rosie_000

Exercise 16: Make a password generator, with a mix of lowercase and uppercase letters, numbers and symbols
"""

import random



"""def passwordGen(x):
    char = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    passw = random.sample(char,x)
    passw = ''.join(passw)
    print passw

passwordGen(int(raw_input("How long do you want your password to be?: ")))"""

        
"""Extra: Give the user the option to choose a weak password"""

def passstrGen(x):
    while True:
        weakchar = ['password','sausage','fluffy','batman','swordfish','birthday']
        medchar = "abcdefghijklmnopqrstuvwxyz0123456789"
        char = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if x == "weak":
            wpass = random.choice(weakchar)
            print wpass
            break
        elif x == "medium":
            y = int(raw_input("How long do you want your password to be?: "))
            mpass = random.sample(medchar,y)
            mpass = ''.join(mpass)
            print mpass
            break
        elif x == "strong":
            y = int(raw_input("How long do you want your password to be?: "))
            passw = random.sample(char,y)
            passw = ''.join(passw)
            print passw
            break
        else:
            x = raw_input("I'm sorry, you did not give a valid strength. Please try again! ")

passstrGen(raw_input("Generate your password! Type 'weak' for a weak password, 'medium' for a medium strength password, and 'strong' for a strong password: "))
        
    
    