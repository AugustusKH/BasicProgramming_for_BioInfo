# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:38:29 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 3. GPA

print("This program computes your GPA.")
print("Please enter your completed courses.")
print("Terminate your entry by entering 0 credits.")
total_score = 0
total_credit = 0

while True:
  credit = int(input("Credits? "))
  if credit == 0:
    break
  else:
    grade = input("Grade? ")
    if grade == "A":
      score = 4.0
    elif grade == "A-":
      score = 3.7
    elif grade == "B+":
      score = 3.3
    elif grade == "B":
      score = 3.0
    elif grade == "B-":
      score = 2.7
    elif grade == "C+":
      score = 2.3
    elif grade == "C":
      score = 2.0
    elif grade == "C-":
      score = 1.7
    elif grade == "D+":
      score = 1.3
    elif grade == "D":
      score = 1.0
    else:
      score = 0
    total_score = total_score + (credit * score)
    total_credit = total_credit + credit

if total_credit != 0:
  GPA = total_score/total_credit
  print("Your GPA is", format(GPA,".2f"))