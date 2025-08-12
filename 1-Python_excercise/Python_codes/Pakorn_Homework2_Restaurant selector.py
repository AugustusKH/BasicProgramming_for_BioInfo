# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Printing patterns
# 1a. Write a program that uses nested loops to draw this pattern:

n = 1
m = 7

while n <= 7:
  while m >= 1:
    print("*" * m)    
    m = m - 1
  n = n + 1