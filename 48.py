# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 20:38:50 2022

@author: symmetrybreaker
"""

#   Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000

number = 0

for i in range(1,1001):
    number += (i ** i)
    
print("The last 10 digits of the series are:", str(number)[-10:])    