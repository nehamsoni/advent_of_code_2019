#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:38:24 2019

@author: nehamsoni
"""
import sys
f=open('day8Input.txt','r')
line =f.readline()
line=list(line.strip('\n'))
layers=[]
while len(line)>0:
    layers.append(line[:150])
    line=line[150:]
ans=0
min0=sys.maxsize
for _ in layers:
    if _.count('0')<min0:
        min0=_.count('0')
        ans=_.count('1')*_.count('2')
print(ans,"part1")    
finallayer=[]
for i in range(0,150):
    for lay in layers:
        if lay[i]=='1' or lay[i]=='0':
            finallayer.append(lay[i])
            break
        else:
            continue
for t in range(len(finallayer)):
    if finallayer[t]=='0':
        finallayer[t]=' '
    else:
        finallayer[t]='#'
def print_final_layer():
    global finallayer
    for k in range(6):
        print(''.join(finallayer[:25]),end='\n')
        finallayer=finallayer[25:]
        
print_final_layer()