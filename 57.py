# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 21:06:30 2022

@author: symmetrybreaker
"""

#   In the first 1000 expansions of the sqrt2 infinite continued fraction, how many fractions contain a numerator larger than the denominator?

import numpy as np
import math 
from math import sqrt

def root2expansion(n):
    numerator = ((1/2))((1 - (math.sqrt(2)))**n + (1 + (math.sqrt(2))**n))
    return numerator