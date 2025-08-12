# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:01:50 2020

@author: hp
"""

outfile = open("protein.txt","r")
r = outfile.readline().strip()
st = ""

while r != "":
    st = st + r
    r = outfile.readline().strip()
    
outfile.close()

for i in st[224:319]:
    print(i)