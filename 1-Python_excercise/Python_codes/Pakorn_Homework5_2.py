# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:43:51 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. Average Steps Taken

def read():
    outfile = open("steps.txt", "r")    
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    name_month = ["January", "Febuary", "March", "April", "May", "June", \
                  "July", "August", "September", "October", "November", \
                  "December"]
    mean = []
    total = 0
    cnt = 1    
    
    for i in month:
        while cnt <= i: 
            rfile = outfile.readline().strip()
            num_step = int(rfile)
            total = total + num_step
            cnt = cnt + 1            
        avr = total/(cnt-1)
        mean.append(avr)
        total = 0
        cnt = 1  
    outfile.close()
     
    for j in range(12):
        print("The average steps in", name_month[j], "is", format(mean[j], ".2f"))
    
read()       
        