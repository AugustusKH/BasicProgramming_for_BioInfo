# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 2. Rock, Paper, Scissors Game


def game():
  import random
  comp_value = random.randint(1,3)
  comp = ""
  if comp_value == 1:
    comp = "Rock"
  elif comp_value == 2:
    comp = "Paper"
  elif comp_value == 3:
    comp = "Scissors"
  
  player = input("Enter rock (R), paper (P), or scissors (S): ")
  player_value = 0
  if player == "R":
    player_value = 1
  elif player == "P":
    player_value = 2
  elif player == "S":
    player_value = 3  

  while comp_value == player_value:
    print("Computer:", comp)
    import random
    comp_value = random.randint(1,3)

    if comp_value == 1:
      comp = "Rock"
    elif comp_value == 2:
      comp = "Paper"
    elif comp_value == 3:
      comp = "Scissors"

    player = input("Enter rock (R), paper (P), or scissors (S) again: ")

    if player == "R":
      player_value = 1
    elif player == "P":
      player_value = 2
    elif player == "S":
      player_value = 3

  print("Computer:", comp)    

  if player == "R" and comp == "Paper":
    print("Computer wins!")
  elif player == "R" and comp == "Scissors":
    print("You win!")
  elif player == "P" and comp == "Rock":
    print("You win!")
  elif player == "P" and comp == "Scissors":
    print("Computer wins!")
  elif player == "S" and comp == "Rock":
    print("Computer wins!")
  elif player == "S" and comp == "Paper":
    print("You win!")

def main():
  game()
  question = input("Do you want to play again (y or n)?: ")

  while True:
    if question == "n":
      break
    else:
      game()
      question = input("Do you want to play again (y or n)?: ")

main()