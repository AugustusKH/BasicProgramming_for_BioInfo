# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:42:26 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Word Index

def w_index():
    file = input("Enter a file name: ")
    infile = open(file, "r")        
    word_dict = {}
    rfile = infile.readline().strip()
    cnt = 1
    
    while rfile != "":
        key = rfile.split()               
        for i in key:
            if i not in word_dict:
                word_dict[i] = [cnt]
            elif i in word_dict:
                word_dict[i].append(cnt)
        rfile = infile.readline().strip()
        cnt = cnt + 1
        
    infile.close()
        
    for (k,v) in word_dict.items():
        print(k+": ", end="")
        for j in v:
            print(j, end=" ")
        print()
    
w_index()
        
    

