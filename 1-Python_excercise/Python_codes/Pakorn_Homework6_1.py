# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:40:24 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Driver’s License Exam

def evaluation():
    name_file = input("Enter a file of student's answers: ")
    lst_correct = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", \
                   "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    right_cnt = 0
    wrong_cnt = 0
    lst_test = []
    lst_qwrong = []
    outfile = open(name_file, "r")
    ana = outfile.readline().strip()
    
    while ana != "":
        lst_test.append(ana)
        ana = outfile.readline().strip()
        
    outfile.close()
    
    for i in range(20):
        if lst_test[i] == lst_correct[i]:
            right_cnt = right_cnt + 1
        else:
            wrong_cnt = wrong_cnt + 1
            lst_qwrong.append(i+1)
            
    if right_cnt >= 15:
        print("Pass")
    else:
        print("Fall")
        
    print("Number of correctly answer:", right_cnt)
    print("Number of incorrectly answer:", wrong_cnt)
    
    if wrong_cnt > 0 and wrong_cnt <= 1:
        print("A question you got wrong was")
        print(lst_qwrong[0])
    elif wrong_cnt > 1:
        print("Questions you got wrong were")
        for j in lst_qwrong:
            print(j)
    
evaluation()