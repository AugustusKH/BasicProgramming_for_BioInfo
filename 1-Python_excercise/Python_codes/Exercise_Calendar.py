# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:42:21 2020

@author: hp
"""

first_d = int(input("Enter first day of the month (Sunday = 0, Monday = 0 and so on): "))
num_d = int(input("Enter number of days in the month: "))
n = first_d

print()
print("Sun","\t","Mon","\t","Tue","\t","Wed","\t","Thur","\t","Fri","\t","Sat")

for i in range(1,num_d + 1):
  if n <= 6:
    if i == 1:
      print("\t" * (first_d*2), i, end="")
    else:
      print("\t"*2, i, end="")
  elif n > 6:
    print()
    n = 0
    print(i, end="")
  n = n + 1
  