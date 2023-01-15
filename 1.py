# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 22:27:16 2022

@author: symmetrybreaker
"""

import numpy as np
from numpy import *

#   Create a list and populate it with the natural numbers below 1000

natural_num_range = range(1000)
natural_num_list = []

for i in natural_num_range:
    natural_num_list.append(i)

#   Find the numbers which are multiples of 3 or 5 and put them in another list for later

valid_multiples = []

for i in natural_num_range:
    if natural_num_list[i] % 3 == 0:
        valid_multiples.append(i)
    elif natural_num_list[i] % 5 == 0:
        valid_multiples.append(i)
    else:
        i += 1

#   Sum the multiples and display the answer

answer = sum(valid_multiples)

print("The sum of the natural multiples of 3 and 5 below 1000 is:", answer)