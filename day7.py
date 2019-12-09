#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:19:37 2019

@author: nehamsoni
"""
from day5 import main
def comb(arr):
    if len(arr)==2:
        return [arr,arr[::-1]]
    else:
        ans=[]
        for a in arr:
            cop=arr[:]
            cop.remove(a)
            t=comb(cop)
            for j in t:
                ans.append([a]+j)
        return ans
        
def res(arr):
#    f=open('day7Input.txt','r')
    t=0
    for jo in arr:
        a=[t,jo]
        t=main('day7Input.txt',a)
        t=t[-1]
    return t
     
lis=comb([0,1,2,3,4])
ans=0
for i in lis:
    jup=res(i)
    if jup>ans:
        ans=jup
print(ans)