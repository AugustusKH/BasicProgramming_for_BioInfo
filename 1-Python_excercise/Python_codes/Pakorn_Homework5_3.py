# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:11:57 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 3. Average of Numbers and Exception Handling

def read():
    while True:
        try:
            file = input("Enter a file name: ")
            outfile = open(file, "r")
            break
                        
        except Exception as err:
            print(err)
            
    rfile = outfile.readline().strip()
    cnt = 0
    total = 0    
    
    while rfile != "":
        while True:
            cnt = cnt + 1
            try:
                value = int(rfile)
                break
            except Exception as er:
                print(er)
                rfile = outfile.readline().strip()            
        total = total + value
        rfile = outfile.readline().strip()
    
    outfile.close()      
    mean = total/cnt
    
    print("The average is", mean)
        
read()
