# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:33:41 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Time Calculator

time = int(input("Enter number of second: "))

if time >= 86400:
  day = time//86400
  if (time%86400) >= 3600:
    hour = (time%86400)//3600
    if ((time%86400)%3600) >= 60:
      min = (((time%86400)%3600))//60
      sec = (((time%86400)%3600))%60
      print(day, "days", hour, "hours", min, "minutes", sec, "seconds")
    else:
      sec = (time%86400)%3600
      print(day, "days", hour, "hours", sec, "seconds")
  else:
    if (time%86400) >= 60:
      min = (time%86400)//60
      sec = (time%86400)%60
      print(day, "days", min, "minutes", sec, "seconds")
    else:
      sec = time%86400
      print(day, "days", sec, "seconds")
elif time >= 0:
  if time >= 3600:
    hour = time//3600
    if (time%3600) >= 60:
      min = (time%3600)//60
      sec = (time%3600)%60
      print(hour, "hours", min, "minutes", sec, "seconds")
    else:
      sec = time%3600
      print(hour, "hours", sec, "seconds")   
  else:
    if time >= 60:
      min = time//60
      sec = time%60
      print(min, "minutes", sec, "seconds")
    else:
      sec = time
      print(sec, "seconds") 
else:
  print("Calculation is error due to negative values")