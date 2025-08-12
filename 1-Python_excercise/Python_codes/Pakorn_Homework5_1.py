# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:06:31 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Word List File Writer and Reader

def write():
    infile = open("word.txt", "w")
    number = int(input("Enter a number of word you want to write to a file: "))
    n = 1
    
    while n <= number:
        word = input("Enter a word: ")
        infile.write(word + "\n")
        n = n + 1
        
    infile.close()
    
write()

def read():
    outfile = open("word.txt", "r")
    rfile = outfile.readline().strip()
    cnt_word = 0
    cnt_char = 0
    longest = ""
    
    while rfile != "":
        if len(rfile) > len(longest):
            longest = rfile
        for i in rfile:
            cnt_char = cnt_char + 1
        cnt_word = cnt_word + 1
        rfile = outfile.readline().strip()
    
    outfile.close()    
    mean = cnt_char/cnt_word
    
    print("The number of word in file:", cnt_word)
    print("The longest word in the file:", longest)
    print("The average length of all of the words in the file:", format(mean,".2f"))
    
read()
        
    