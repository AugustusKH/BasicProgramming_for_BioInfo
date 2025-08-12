# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:58:17 2020

@author: hp
"""

first_d = int(input("Enter first day: "))
year = int(input("Enter year: "))
lst_month = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
num_d = 0

def calendar_month():
    print()
    print("\t"*4, month, year)
    print("Sun","\t","Mon","\t","Tue","\t","Wed","\t","Thur","\t","Fri","\t","Sat")
    global first_d
    n = first_d
          
    for i in range(1,num_d + 1):
      if n <= 6:
        if i == 1:
          print("\t" * (first_d*2), i, end="")
        else:
          print("\t"*2,i,end="")
      elif n > 6:
        print()
        print(i,end="")
        n = 0    
      n = n + 1

    if n == 7:
      first_d = 0  
    else:
      first_d = n
      
for month in lst_month:
  if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    num_d = 31
    calendar_month()
    print()
  elif month == "April" or month == "June" or month == "September" or month == "November":
    num_d = 30
    calendar_month()
    print()
  elif month == "Febuary":
    num_d = 29
    calendar_month()
    print()