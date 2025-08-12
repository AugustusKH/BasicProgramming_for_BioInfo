# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:40:24 2020

@author: hp
"""

# Pakorn Sagulkoo 6380064520
# 3. Lo Shu Magic Square

def Lo_Shu():
    import random

    lst = [1,2,3,4,5,6,7,8,9]
    m_square = [[0,0,0],[0,0,0],[0,0,0]]
    cnt = 1

    while cnt <= 100000:
        for i in range(len(m_square)):
            for j in range(len(m_square[0])):
                r = random.sample(lst,1)
                m_square[i][j] = r[0]
                lst.remove(r[0])  

        if m_square[0][0] + m_square[0][1] + m_square[0][2] == 15:
            if m_square[1][0] + m_square[1][1] + m_square[1][2] == 15:
                if m_square[2][0] + m_square[2][1] + m_square[2][2] == 15:
                    if m_square[0][0] + m_square[1][0] + m_square[2][0] == 15:
                        if m_square[0][1] + m_square[1][1] + m_square[2][1] == 15:
                            if m_square[0][2] + m_square[1][2] + m_square[2][2] == 15:
                                if m_square[0][0] + m_square[1][1] + m_square[2][2] == 15:
                                    if m_square[0][2] + m_square[1][1] + m_square[2][0] == 15:
                                        print("Simulation #",cnt,"is a Lo Shu Magic Square")
                                        print(m_square)

        cnt = cnt + 1
        lst = [1,2,3,4,5,6,7,8,9]    
        
Lo_Shu()