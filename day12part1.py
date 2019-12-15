#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:20:18 2019

@author: nehamsoni
"""

import numpy as np
moon=[[-6, 2, -9],[12, -14, -4],[9, 5, -6],[-1, -4, 9]]
moon_pos=np.matrix(moon,dtype='float64')
moon_vel=np.matrix(np.zeros((4,3)))
def change(pos):
    global moon_vel
    boo=[]
    def choo(a):
        lee=[]
        for i in a:
            lee.append(sum(np.transpose(a>i).tolist()[0])-sum(np.transpose(a<i).tolist()[0]))
        return np.transpose(np.matrix(lee))     
    for i in range(3):
        boo.append(choo(pos[:,[i]]))
    moon_vel=np.hstack(boo)+moon_vel
    return moon_vel
blah=[[[],[],[]],[[],[],[]],[[],[],[]]]           
for k in range(1000):
    moon_pos+=change(moon_pos)
    for p in range(3):
        for q in range(3):
            blah[p][q].append(moon_pos[p,[q]].tolist()[0][0])
moon_pos=np.absolute(moon_pos).sum(axis=1)
moon_vel=np.absolute(moon_vel).sum(axis=1).transpose()
print(moon_vel*moon_pos)