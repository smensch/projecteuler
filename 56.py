# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 20:50:45 2022

@author: symmetrybreaker
"""

#   Find the maximum digital sum of a^b, where a,b < 100.

import numpy as np

#   Iterate through the various possibilities while keeping a 'high water mark' to compare against.  Print high values as they are found, the final set being the maximum digital sum.

highscore = 0

def digitalsum(n):
    dsum = 0
    for achar in str(n):
        dsum += int(achar)
    return dsum

for i in range(1,100):
    for j in range(1,100):
        if digitalsum(i ** j) > highscore:
            highscore = digitalsum(i ** j)
            print(i, j, highscore)