# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Printing patterns
# 1b. Write a program that uses nested loops to draw this pattern:

for i in range(1,7):
  for j in range(0,i+1):
    if j == 0 or j == i:
      print("#", end="")
    else:
      print(" ", end="") 
  print()