# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:40:28 2020

@author: hp
"""

def count_list():
  n = input("Enter a sentance: ")
  lst = n.split()
  new_lst = []

  for i in lst:
    if i != "The" and i != "the":
      cnt = len(i)
      new_lst.append(cnt)

  print(new_lst)

count_list()