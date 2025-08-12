# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Alphabetic Telephone Number Translator

def numbertrans():
    data = input("Enter phone number: ")
    re_dat = ""
    
    for i in data:
        if i != "-":
            re_dat = re_dat + i
    
    dat_up = re_dat.upper()
    trans_num = ""
    
    for j in dat_up:
        if j == "A" or j == "B" or j == "C":
            j = "2"
        elif j == "D" or j == "E" or j == "F":
            j = "3"
        elif j == "G" or j == "H" or j == "I":
            j = "4"
        elif j == "J" or j == "K" or j == "L":
            j = "5"
        elif j == "M" or j == "N" or j == "O":
            j = "6"
        elif j == "P" or j == "Q" or j == "R" or j == "S":
            j = "7"
        elif j == "T" or j == "U" or j == "V":
            j = "8"
        elif j == "W" or j == "X" or j == "Y" or j == "Z":
            j = "9"
        else:
            j = j
            
        trans_num = trans_num + j
            
    final_num = ""
    
    if len(trans_num) == 10:
        final_num = trans_num[0:3] + "-" + trans_num[3:6] + "-" + trans_num[6:]
    elif len(trans_num) == 11:
        final_num = trans_num[0] + "-" + trans_num[1:4] + "-" + trans_num[4:7] + \
                    "-" + trans_num[7:]
        
    print(final_num)
        
numbertrans()  