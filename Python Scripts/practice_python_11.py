# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 20:25:21 2017

@author: rosie_000

Exercise 11: Function to check if a number is prime or not
"""

        
def prime_check(a):
    ra = range(2,a)
    divisors = [i for i in ra if a%i == 0]
    if divisors != []:
        print("Divisors are "+ str(divisors))
        print(str(a)+" is not a prime.")
    elif divisors == []:
        print(str(a)+" is a prime.")
    

prime_check(10)
        
            
        