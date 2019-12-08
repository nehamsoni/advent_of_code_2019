#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:18:59 2019

@author: nehamsoni
"""

import networkx as nx
G=nx.Graph()
elist=[]
alle={'COM'}
f= open('day6Input.txt','r')
for line in f:
    a,b=line.strip('\n').split(')')
    elist.append(line.strip('\n').split(')'))
    alle.add(a)
    alle.add(b)
    
G.add_edges_from(elist)
ans=0
for _ in alle:
    ans+=len(nx.dijkstra_path(G,'COM',_))-1
print(ans,"part1")
print(len(nx.dijkstra_path(G,'YOU','SAN'))-3,"part2")