# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 17:34:51 2016

@author: Caroline
"""

#Assuming s is already set
s = input("s=")
count = 0

while 'bob' in s:
    count += 1 
    s = s[(s.find('bob') + 2):]
    #finds the index of the last bob, adds 2 (for letters 'o' and 'b')
    # will add a count if bob is found, since it takes away only first b and o
    #reoccuring patterns will not be overlooked
print("Number of times bob occurs is:",count) 

# have to iterate a range in for loop