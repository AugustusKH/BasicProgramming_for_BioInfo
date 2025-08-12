# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:03:24 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. File Analysis

def file_ana():
    file1 = input("Enter file 1: ")
    file2 = input("Enter file 2: ")
    infile1 = open(file1, "r")
    infile2 = open(file2, "r")
    lst1 = []
    lst2 = []
    rfile1 = infile1.readline().strip()
        
    while rfile1 != "":
        sp1 = rfile1.split()
        lst1.extend(sp1)
        rfile1 = infile1.readline().strip()
        
    infile1.close()
    set1 = set(lst1)
    rfile2 = infile2.readline().strip()
    
    while rfile2 != "":
        sp2 = rfile2.split()
        lst2.extend(sp2)
        rfile2 = infile2.readline().strip()
        
    infile2.close()
    set2 = set(lst2)
    
    intersc_set = set1 & set2
    union_set = set1 | set2
    only1 = set1 - set2
    only2 = set2 - set1
    only_both = set1 ^ set2
    
    print("--------A list of all the unique words contained in both files--------")   
    for a in intersc_set:
        print(a,end=" ")
    print("\n")
    
    print("--------A list of the words that appear in both files--------")   
    for b in union_set:
        print(b,end=" ")
    print("\n")
    
    print("--------A list of the words that appear in the first file but not the second--------")   
    for c in only1:
        print(c,end=" ")
    print("\n")
    
    print("--------A list of the words that appear in the second file but not the firstA list of the words that appear in either the first or second file, but not both--------")   
    for d in only2:
        print(d,end=" ")
    print("\n")
    
    print("--------A list of the words that appear in either the first or second file, but not both--------")   
    for e in only_both:
        print(e,end=" ")
    print("\n")
    
file_ana()
        
    