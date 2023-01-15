# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:27:02 2022

@author: symmetrybreaker
"""

#   Find the sum of the digits in the number 100!

import math
from math import *

import numpy as np
from numpy import *

#   Create the number and an empty accumulator.  Make the number into a string and iteratively add the int'd characters to the accumulator

number = math.factorial(100)

sum = 0

number = str(number)

for achar in number:
    sum += int(achar)
    
print("The sum of the digits in the number 100! is:", sum)
