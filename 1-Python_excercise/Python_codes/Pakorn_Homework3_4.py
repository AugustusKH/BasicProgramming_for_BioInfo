# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 4. Mean and standard deviation.

sum = 0
sum_square = 0
n = 0

while True:
  infor = input("Enter number: ")
  if infor == "Q":
    break
  else:
    num = float(infor)
    sum = sum + num
    sum_square = sum_square + (num**2)
    n = n + 1

mean = sum/n
sd = ((sum_square-((sum**2)/n))/(n-1))**0.5

print("average is", format(mean,".2f"), "sd is", format(sd,".2f"))