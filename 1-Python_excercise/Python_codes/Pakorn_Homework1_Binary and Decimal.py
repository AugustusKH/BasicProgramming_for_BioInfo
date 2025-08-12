# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:29:14 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 3. Binary and decimal conversion

A = input("Enter an eight digit binary number: ")
Bi = int(A)

De1 = (Bi//1e7)*(2**7)
De2 = ((Bi//1e6)%10)*(2**6)
De3 = ((Bi//1e5)%10)*(2**5)
De4 = ((Bi//1e4)%10)*(2**4)
De5 = ((Bi//1e3)%10)*(2**3)
De6 = ((Bi//1e2)%10)*(2**2)
De7 = ((Bi//10)%10)*2
De8 = Bi%10

Sum_De = De1+De2+De3+De4+De5+De6+De7+De8

print("The decimal equivalent of ", A, " is ", int(Sum_De), ".", sep='')
