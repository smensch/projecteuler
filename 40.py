# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:16:37 2022

@author: symmetrybreaker
"""

#   Find the value of the expression d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#   Where dn is the nth digit of the fractional part of the irrational decimal fraction 0.123456789101112131415161718192021...

#   Make a list by iteratively counting to 500000, then concatenate all the values of the list into one giant string, which will mimic the irrational fraction.
#   The 0 in numlist makes the indices of the string match those of the dn terms for the final calculation

numlist = [0]
numstr = ""

for i in range(500000):
    numlist.append(i+1)
    
for i in range(500000):
    numstr = numstr + str(numlist[i])
        
#   Calculate the product of the specific terms and display the answer    
    
answer = int(numstr[1]) * int(numstr[10]) * int(numstr[100]) * int(numstr[1000]) * int(numstr[10000]) * int(numstr[100000]) * int(numstr[1000000])

print("The product of the expression is:", answer)

