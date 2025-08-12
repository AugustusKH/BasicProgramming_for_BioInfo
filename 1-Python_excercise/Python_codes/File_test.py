# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:03:02 2020

@author: hp
"""

def openfile():
    w_file = open("grant.txt", "w")
    ID = input("Enter student ID: ")
    
    while ID != "":
        tuition = input("Enter tuition fee receiving status (Y/N): ")
        stipend = input("Enter stipend receiving status (Y/N): ")
        w_file.write(ID + "\t")
        w_file.write(tuition + "\t")
        w_file.write(stipend + "\n")
        ID = input("Enter student ID: ")
    
    w_file.close()
    
def anafile():
    r_file = open("grant.txt", "r")
    infile = r_file.readline().strip()
    tui = 0
    stip = 0
    both = 0
    none_both = 0
    string = ""
    
    while infile != "":
        for i in infile:
            if i != "\t":
                string = string + i
                
        if string[10] == "Y" and string[11] == "Y":
            both = both + 1
        elif string[10] == "Y" and string[11] == "N":
            tui = tui + 1
        elif string[10] == "N" and string[11] == "Y":
            stip = stip + 1
        else:
            none_both = none_both + 1
            
        infile = r_file.readline().strip()
        string = ""
    r_file.close()
        
    value_tui = tui * 21000
    value_stip = stip * 8000
    value_both = both * 29000
    total_value = value_tui + value_stip + value_both
    
    print("Both:", both)
    print("Tuition fee only:", tui)
    print("Stipend only:", stip)
    print("Neither:", none_both)
    print("budget required:", total_value)
    
anafile()
            
                
            
            
            
            
            
            
            