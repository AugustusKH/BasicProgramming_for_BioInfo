# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:14:46 2020

@author: hp
"""

Thai_pop_open=open("ThaiPopulation.txt","r")
Thai_pop_open_read=Thai_pop_open.readline().strip()
year_list = []
pop_list = []

while Thai_pop_open_read != "":
    year = Thai_pop_open_read.split()[0]      
    pop = Thai_pop_open_read.split()[1]
    year_list.append(year)
    pop_list.append(pop)         
    Thai_pop_open_read=Thai_pop_open.readline().strip()
    
Thai_pop_open.close() 
total_year = len(year_list)
opperate_pop = 0
accu_pop = 0
accu_list = []

for i in range(total_year-1):
    opperate_pop=int(pop_list[i+1])-int(pop_list[i])
    accu_list.append(opperate_pop)
    accu_pop=accu_pop+opperate_pop
    
print(accu_list)
# print('Average annual change:',  accu_pop / (total_year-1))
# print('Greatest increase:',max(accu_list))
# print('Smallest increase: ',min(accu_list))