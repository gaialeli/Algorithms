
"""
Created on Fri Sep 25 16:21:15 2020

@author: gaialeli

Write a function that takes a list of characters and reverses the letters in place.

SOLUTION: swap the 1st el with last el., the 2nd el with 2nd to last and so on
"""

def reverse(list_chars):
    
    left_index = 0
    right_index = len(list_chars) -1 
    
    while left_index < right_index:
        
        #swap characters
        list_chars[left_index], list_chars[right_index] = list_chars[right_index], list_chars[left_index]
        
        #move to the center of the list
        left_index = left_index +1
        right_index = right_index-1
        
    return list_chars
        

#input
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l']

print('Input:', my_list)

#output
my_reversed_list = reverse(my_list)

print('Reversed input:', my_reversed_list)



