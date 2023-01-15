# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:48:21 2022

@author: symmetrybreaker
"""

import numpy as np

#   Calculate  the sum of the 'name scores' of the given list of names, these scores are equal to the alphabebetic vlaue of each letter, summed, multiplied by the names' position in the list when it has been alphabetized

#   Create and alphabet dictionary to assign number values to each letter of the alphabet

alphabet_dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
    }

#   Import the namelist and delimit it.
#   Elide the " off of the names

namelist = np.loadtxt("p022_names.txt", dtype = str, delimiter = ",")

for i in range(len(namelist)):
    namelist[i] = namelist[i][1:-1]

#   Alphabetize the list
    
namelist = sorted(namelist)

#   Create a scorelist

scorelist = []
    
#   For each name in the namelist, use the dictionary to parse the letter values and populate the scorelist with their values.  Afterwards, iterate again to multiply the scores by their respective positions in the list

for i in range(len(namelist)):
    score = 0
    for achar in namelist[i]:
        score += alphabet_dict.get(achar)
    scorelist.append(score)
 
for i in range(len(scorelist)):
    scorelist[i] = (i+1) * scorelist [i] 
    
#   Print the answer    
    
answer = sum(scorelist)

print("The total of all the name scores in the file is:", answer)

    