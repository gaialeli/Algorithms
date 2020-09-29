
"""
Created on Sat Sep 26 10:35:07 2020

REVERSE WORDS: This function reverse the word order of a string, in place

ASSUMPTION: the message contains only words and 1 space inbetween words
@author: gaialeli

e.g.
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

'steal pound cake'

SOLUTION

STEP 1: reverse the letters in place: will give the correct words order but each word will be backwords
        the reverse_characters function swaps the 1st el with the last, the 2nd with the 2nd last and so on.
        
SREP 2: reverse the characters in each word. Empty space character ' ' will tell where a word ends.

"""


# reverse each word in place
def reverse_words(message):
    
    reverse_characters(message, 0, len(message)-1)
    
    # we assume that the first char is not a space
    current_word_start_index = 0
    
    # NOTE: why +1? I need to go +1 over the lenght of the message in order to use (i-1) in the reverse_characters call in any case 
    #       by switching the order of the or elements I can get away with it.
    for i in range(len(message)+1):
        
        # where the current word stops? at at the end of my message or at the space char ' '
        if (i == len(message)) or (message[i] == ' '):
            
            reverse_characters(message, current_word_start_index, i-1)
            
            # if the message is not finished the next word start in =1 charcater
            current_word_start_index = i + 1
            
    return message
            
            
# reverse characters in place  
def reverse_characters(message, left_index,right_index):
    
    while left_index < right_index:
        
        message[left_index], message[right_index] = message[right_index],  message[left_index]
        
        left_index +=1 
        right_index -=1
        
    return message # remember we are working inplace
        

#input
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

# function call
reverse_words(message)

# Print: 'steal pound cake'
print(''.join(message))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
     
     

