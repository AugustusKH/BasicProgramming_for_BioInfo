# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 1. Random Number Guessing Game


def rand_game():
  import random
  rand = random.randint(1,100)
  value = int(input("Please guess what a number is: "))
  n = 1

  while True:
    if value == rand:
      break
    elif value < rand:
      print("Too low, try again")
    else:
      print("Too high, try again")
    n = n + 1
    value = int(input("Please guess what a number is: "))

  print("Congratulations! You use", n, "attemps")

def main():
  rand_game()
  question = input("Do you want to continue (y or n)?:") 

  while True:
    if question == "n":
      break
    else:
      rand_game()
      question = input("Do you want to continue (y or n)?:") 

main()