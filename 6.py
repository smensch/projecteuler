# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:24:55 2022

@author: symmetrybreaker
"""

#   Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum

first_hundred_naturals = []

for i in range(1,101):
    first_hundred_naturals.append(i)

#   Sum of the squares

square_sum = 0

for i in range(100):
    square_sum += first_hundred_naturals[i] ** 2
    
#   Square the sum

sum_squared = (sum(first_hundred_naturals)) ** 2

#   Calculate the difference between "square_sum" and "sum_squared", print the answer

answer = sum_squared - square_sum

print("The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is:", answer)

