# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:01:31 2022

@author: symmetrybreaker
"""

import numpy as np
from numpy import *

#   Create a list and populate it with the terms in the Fibonacci sequence whose values do not exceed 4e6

fibonacci = [1,2]

for i in range(100000):
    if (fibonacci[i+1] + fibonacci[i]) <=4000000:
        fibonacci.append(fibonacci[i+1] + fibonacci[i])
    else:
        break
    
#   Create a list for even-valued terms and populate it

fibonacci_evens = []

for i in range(len(fibonacci)):
    if (fibonacci[i] % 2) == 0:
       fibonacci_evens.append(fibonacci[i])
       
#   Sum the terms and display the answer       
       
answer = sum(fibonacci_evens) 

print("The sum of even-valued Fibonacci sequence terms whose value does not exceed 4 million is:", answer)      