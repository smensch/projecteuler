# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:54:31 2022

@author: symmetrybreaker
"""

#   Of the list of provided words, how many are triangle words?
#   A triangle word is one whose word value (summed letter value) is equal to a term of the sequence of triangle numbers
#   The triangle sequence is tn = .5n(n+1)

import numpy as np

#   Import word list and prune commas and quotations

wordlist = np.loadtxt("p042_words.txt", dtype = str, delimiter = ",")

for i in range(len(wordlist)):
    wordlist[i] = wordlist[i][1:-1]

#   Create alphabet dictionary to calculate word values with

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

#   Create a triangle sequence to compare to, we may stop at n= ~25 due to word length

triangle_sequence = []

for i in range(100):
    triangle_sequence.append(int(.5 * i * (i+1)))

#   Calculate the word scores

scorelist = []
       
for i in range(len(wordlist)):
    score = 0
    for achar in wordlist[i]:
        score += alphabet_dict.get(achar)
    scorelist.append(score)   

#   Create a dictionary pairing the scores and words, this is unused due to a revision of method during solving

#word_dict = dict(zip(scorelist, wordlist)) 

#triangle_words = []

#   Count the number of triangle sequence occurences in the score list and print the answer

answer = 0
         
for number in triangle_sequence:
    answer += scorelist.count(number)
    
#   Print answer

print("There are", answer, "triangle words in the provided text file.")