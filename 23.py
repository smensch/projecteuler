# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:33:21 2022

@author: symmetrybreaker
"""

import numpy as np

#   What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

#   Create a list for the Fibonacci sequence

fibonacci = [0,1]

for i in range(10000):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2] 
    fibonacci.append(fibonacci[i])
 
#   Make the indices of the list match the formalism of the question  
 
zero = [0,0]

fibonacci = zero + fibonacci     

#   Iterate over the list and check the length of each term until one of a length 1000 is found, then print the corresponding index   

answer = 0

for i in range(len(fibonacci)):
    while len(str(fibonacci[i])) < 1000:
        i += 1
        if len(str(fibonacci[i])) == 1000:
            answer = i
        break

#   Print the answer

print("The index of the first 1000-digit length term in the Fibonacci sequence is:", answer)    