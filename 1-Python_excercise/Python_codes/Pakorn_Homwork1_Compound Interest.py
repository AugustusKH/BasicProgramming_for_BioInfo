# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:42:58 2020

@author: hp
"""
# Pakorn Sagulkoo 6380064520
# 2. Compound interest

P = float(input("Enter the amount of principal originally deposited: "))
r = float(input("Enter the annual interest rate: "))/100
n = int(input("Enter the number of times per year that the interest is compounded: "))
t = float(input("Enter the number of years: "))

A = P*((1+(r/n))**(n*t))

print("The amount of money that will be in the account after ", int(t), " years is $", format(A, ',.2f'), sep='')