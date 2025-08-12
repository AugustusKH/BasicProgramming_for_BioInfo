# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:25:13 2020

@author: hp
"""

def sum67(lst):
  total = 0
  i = 0
  
  while i < len(lst):
    if lst[i] == 6:
      while True:
        if lst[i] == 7:
          i = i + 1
          break                
        i = i + 1
    else:
      total = total + lst[i]
      i = i + 1        

  print(total)

lst = [2, 2, 6, 7, 7]
sum67(lst)