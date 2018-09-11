# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 11:05:38 2017

@author: rosie_000
Exercise 20: Element Search.
Write a function that takes an ordered list of numbers (a list where the elements are in
 order from smallest to largest) and another number. The function decides whether or not 
 the given number is inside the list and returns (then prints) an appropriate boolean.
"""

import random

a = random.sample(range(20),5)
a.sort()
print a

"""def listbool(o_list, num_find):
    while True:
        for i in o_list:
            if i == num_find:
                return True
        return False"""
            

"""if __name__ =="__main__":
    print listbool(a,input("Give me a number: "))"""
    
"""Extra: do the exercise using a binary search, where you keep splitting the list
into haf until you find the answer"""

"""def listboolbin(o_list,num):
  start_index = 1
  end_index = len(o_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    print middle_index
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = o_list[middle_index]
    if middle_element == num:
      return True
    elif middle_element > num:
      end_index = middle_index
    else:
      start_index = middle_index
  
if __name__=="__main__":
    print listboolbin(a,input("Give me a number: "))"""
    
def binary_search(array, target): #target is 10 for example
    lower = 0 #2;3; 3;
    upper = len(array) #5;5;4
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2  #=2; 3; 4; 3
        val = array[x] #=6, 8, 11, 8
        if target == val:
            return True
        elif target > val: 
            if lower == x: #0=/ 2; 2=/ 3; 3 /= 4; 3 ==3 so break
                break       
            lower = x #==2; 3
        elif target < val: 
            upper = x 

if __name__=="__main__":
    l = [1,4,6,8,11]
    print binary_search(l,input("Give me a number: " ))

    


    
    