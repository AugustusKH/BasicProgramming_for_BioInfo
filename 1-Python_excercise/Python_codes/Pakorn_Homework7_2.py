# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:58:52 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. PowerBall Lottery

def statlot():
    outfile = open("pbnumbers.txt", "r")
    read = outfile.readline().strip()
    lst = []
    
    while read != "":
        s = read.split()
        lst.append(s)
        read = outfile.readline().strip()
        
    outfile.close()
    
    lst_all = []
    lst_number = []
    lst_pb = []
        
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst_all.append(lst[i][j])
            if j != 5:
                lst_number.append(lst[i][j])
            else:
                lst_pb.append(lst[i][j]) 
                
    f_num = []
    f_pb = []
    f_all = []
    cnt_num = 0
    cnt_pb = 0 
    cnt_all = 0
      
    for k in range(1,70):
        for l in lst_number:
            if str(k) == l:
                cnt_num = cnt_num + 1
        f_num.append(cnt_num)
        cnt_num = 0
        
    for m in range(1,27):
        for n in lst_pb:
            if str(m) == n:
                cnt_pb = cnt_pb + 1
        f_pb.append(cnt_pb)
        cnt_pb = 0     

    for o in range(1,70):
        for p in lst_all:
            if str(o) == p:
                cnt_all = cnt_all + 1
        f_all.append(cnt_all)
        cnt_all = 0        
        
    arr_lst = []
    re_arr = []
    
    for q in f_all:
        arr_lst.append(q)
        re_arr.append(q)
        
    arr_lst.sort()  # min to max        
    re_arr.sort(reverse = True) # max to min
    
    max_lst = []
    min_lst = []
    
    r = 0        
    while r < 10:
        order_1 = 1
        while True:
            if ((f_all.index(re_arr[r]) + 1) in max_lst) and r < 10:
                max_lst.append((f_all.index(re_arr[r], f_all.index(re_arr[r]) + order_1)) + 1)
                r = r + 1
                order_1 = order_1 + 1
            elif ((f_all.index(re_arr[r]) + 1) not in max_lst) and r < 10:
                max_lst.append((f_all.index(re_arr[r])) + 1)
                break
            else:
                break
        r = r + 1
        
    s = 0
    while s < 10:
        order_2 = 1
        while True:
            if ((f_all.index(arr_lst[s]) + 1) in min_lst) and s < 10:
                min_lst.append((f_all.index(arr_lst[s], f_all.index(arr_lst[s]) + order_2)) + 1)
                s = s + 1
                order_2 = order_2 + 1
            elif ((f_all.index(arr_lst[s]) + 1) not in min_lst) and s < 10:            
                min_lst.append((f_all.index(arr_lst[s])) + 1)
                break
            else:
                break
        s = s + 1
        
    distance = []
    order_d = []
    
    for t in range(1,70):
        distance.append(lst_all.index(str(t)))
        order_d.append(lst_all.index(str(t)))
        
    order_d.sort()
    order_d.reverse() # max to min overdue
    
    print("The 10 most common numbers and their frequencies")
    
    for u in range(10):
        print(max_lst[u], ":", re_arr[u], sep = "", end = " ")
        
    print("\n")            
    print("The 10 least common numbers and their frequencies")
    
    for v in range(10):
        print(min_lst[v], ":", arr_lst[v], sep = "", end = " ")
        
    print("\n")
    print("The 10 most overdue numbers")
        
    for w in range(10):
        print((distance.index(order_d[w])) + 1, sep = "", end = " ")  
        
    print("\n")
    print("The frequency of each number 1–69")
    
    for x in range(69):
        print(x+1, ":", f_num[x], sep = "", end = " ")
        
    print("\n")
    print("The frequency of each Powerball number 1–26")
    
    for y in range(26):
        print(y+1, ":", f_pb[y], sep = "", end = " ")     
    
statlot()