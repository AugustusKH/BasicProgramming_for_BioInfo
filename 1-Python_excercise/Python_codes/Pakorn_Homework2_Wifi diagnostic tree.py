# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:36:21 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. Wi-Fi Diagnostic Tree

print("Reboot the computer and try to connect.")
Q1 = input("Did that fix the problem?: ")

if Q1 == "yes":
  print("The problem can be fixed")
elif Q1 == "no":
  print("Reboot the router and try to connect.")
  Q2 = input("Did that fix the problem?: ")
  if Q2 == "yes":
    print("The problem can be fixed")
  elif Q2 == "no":
    print("Make sure the cables between the router and modem are plugged in firmly.")
    Q3 = input("Did that fix the problem?: ")
    if Q3 == "yes":
      print("The problem can be fixed")
    elif Q3 == "no":
      print("Move the router to a new location and try to connect.")
      Q4 = input("Did that fix the problem?: ")
      if Q4 == "yes":
        print("The problem can be fixed")
      elif Q4 == "no":
        print("Get a new router.")
      else:
        print("Error in typing, please type it again with yes or no answer")
    else:
      print("Error in typing, please type it again with yes or no answer")
  else:
    print("Error in typing, please type it again with yes or no answer")
else:
  print("Error in typing, please type it again with yes or no answer")