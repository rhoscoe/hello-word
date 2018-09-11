# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 11:16:40 2017

@author: rosie_000

Exercise 13: Write a program that asks the user for how many Fibonacci numbers and generates them
"""

def fibo():
    us = int(raw_input("How many Fibonacci numbers do you want? "))
    c = [0,1]
    while us > 1:
      n = c[-2]
      m = c[-1]
      x = n+m
      c.append(x)
      us -= 1
    del c[0]
    return c

print fibo()