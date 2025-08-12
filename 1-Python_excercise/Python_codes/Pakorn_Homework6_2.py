# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:40:24 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. Population Data

def analys_pop():
    filename = input("Enter a file: ")
    outfile = open(filename, "r")
    rfile = outfile.readline().strip()
    lst = []
    
    while rfile != "":
        file_split = rfile.split()
        lst.append(file_split)
        rfile = outfile.readline().strip()
        
    outfile.close()
        
    lst_year = []
    lst_value = []   

    
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if j == 0:
                lst_year.append(lst[i][j])
            else:
                lst_value.append(lst[i][j])
                
    min = int(lst_value[1]) - int(lst_value[0])
    max = 0     
    year_min = ""
    year_max = ""
    sum_delta = 0
    cnt = 0
     
    for k in range(len(lst_value)-1):
        delta = int(lst_value[k+1]) - int(lst_value[k])
        if delta > max:
            max = delta
            year_max = lst_year[k] + " - " + lst_year[k+1]
        if delta <= min:
            min = delta
            year_min = lst_year[k] + " - " + lst_year[k+1]
             
        sum_delta = sum_delta + delta
        cnt = cnt + 1
         
    avr_delta = sum_delta/cnt
     
    print("Average annual change:", format(avr_delta, ".2f"))
    print("Greatest increase:", year_max)
    print("Smallest increase:", year_min)         
        
analys_pop()