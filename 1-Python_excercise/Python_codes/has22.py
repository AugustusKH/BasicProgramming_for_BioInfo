# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:40:11 2020

@author: hp
"""

def has22(lst):
  n = len(lst)
  cnt = 0
  b = False

  while cnt < (n-1):
    if lst[cnt] == 2 and lst[cnt+1] == 2:
      b = True        
    cnt = cnt + 1

  print(b)

lst = [1, 3, 2, 2]
has22(lst)