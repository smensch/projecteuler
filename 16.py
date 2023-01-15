# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:16:33 2022

@author: symmetrybreaker
"""

#   What is the sum of the digits of the number 2**1000?

import math
from math import *

import numpy as np
from numpy import *

#   Create the number and turn it into a string so we can iterate and add up the int'd characters in the string

number = 2**1000

number = str(number)

sum = 0

for achar in number:
    sum = sum + int(achar)

#   Display our answer

print("The sum of the digits of 2**1000 is:", sum)