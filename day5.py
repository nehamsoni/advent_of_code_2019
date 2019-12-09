#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:20:20 2019

@author: nehamsoni
"""
def main(filename='day5Input.txt',change=10*[1]):  #change to 5 for part_2
    answer=[]
    def full_opcode(n):
        n=list(str(n))
        return [0]*(5-len(n))+list(map(int,n))
        
    pos=0
    f=open(filename,'r')
    arr=f.readline().split(',')
    arr=list(map(int,arr))
    while arr[pos]!=99:
        opcode=full_opcode(arr[pos])
        if opcode[-1]==1:
            ans=0
            param=arr[pos+1:pos+4]
            mode=opcode[:3][::-1]
            for i in range(2):
                if mode[i]==0:
                    ans+=arr[param[i]]
                else:
                    ans+=param[i]
            arr[param[2]]=ans
            pos+=4
            continue
            
        if opcode[-1]==2:
            ans=1
            param=arr[pos+1:pos+4]
            mode=opcode[:3][::-1]
            for i in range(2):
                if mode[i]==0:
                    ans*=arr[param[i]]
                else:
                    ans*=param[i]
            arr[param[2]]=ans
            pos+=4
            continue
            
        if opcode[-1]==3:
            arr[arr[pos+1]]=change.pop() 
            pos+=2
            continue
        
        if opcode[-1]==4:
            if opcode[2]==0:
                answer.append(arr[arr[pos+1]])
            else:
                answer.append(arr[pos+1])
            pos+=2
            continue
        
        if opcode[-1]==7:
            param=arr[pos+1:pos+4]
            mode=opcode[:3][::-1]
            for i in range(2):param[i] = arr[param[i]] if mode[i]==0 else param[i]
            if param[0]<param[1]:
                arr[param[2]]=1
            else:
                arr[param[2]]=0
            pos+=4
            continue
        
        if opcode[-1]==8:
            param=arr[pos+1:pos+4]
            mode=opcode[:3][::-1]
            for i in range(2):param[i] = arr[param[i]] if mode[i]==0 else param[i]
            if param[0]==param[1]:
                arr[param[2]]=1
            else:
                arr[param[2]]=0
            pos+=4
            continue
        
        if opcode[-1]==5:
            param=arr[pos+1:pos+3]
            mode=opcode[:3][::-1]
            for i in range(2):param[i] = arr[param[i]] if mode[i]==0 else param[i] 
            if param[0]!=0:
                pos=param[1]
            else:
                pos+=3
                
        if opcode[-1]==6:
            param=arr[pos+1:pos+3]
            mode=opcode[:3][::-1]
            for i in range(2):param[i] = arr[param[i]] if mode[i]==0  else param[i]
            if param[0]==0:
                pos=param[1]
            else:
                pos+=3
    return answer
            
if __name__ == "__main__":          
    print(main())
    
            
        
    
        
                
            
    