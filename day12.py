#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:38:07 2019

@author: nehamsoni
"""
import numpy as np
from math import gcd
import multiprocessing as mp

def seqperiod(p,arr):
  i=2
  def check(n,m):
    if len(n)<=len(m):
      s=n
      l=m
    else:
       s=m
       l=n
    return l[:len(s)]==s
  while True:
    if check(arr[:i],arr[i:])==True:
      return (p,len(arr[:i]))
    else:
      i+=1
      
pool = mp.Pool(mp.cpu_count())
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


blah=[[[0],[0],[0]],[[],[],[]],[[],[],[]]]           
for k in range(300000):
    moon_pos+=change(moon_pos)
    for p in range(1):
        for q in range(3):
            blah[p][q].append(moon_vel[p,[q]].tolist()[0][0])

app=[]

def collect_result(result):
    global app
    app.append(result)
    
for p,t in enumerate([(0,0),(0,1),(0,2)]):
    pool.apply_async(seqperiod, args=(p, blah[t[0]][t[1]] ), callback=collect_result)
pool.close()
pool.join()

app.sort(key=lambda x: x[0])
results_final = [r for i, r in app]
app=results_final[:]
lcm = app[0]
for i in app[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)