# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:01:58 2020

@author: abasavar
"""
from typing import List

class ReArrangeArray:
    def ArrayData(self,arr: List[int]):
        temp=0
        tempValue=0
        print(avgValue)
        for i in range(len(arr) -1):
            if(arr[i]>arr[i+1]):
                temp=i
        for i in range(temp+1):
            tempValue=arr[i]
            print(tempValue)
            arr[i]=arr[i+temp+1]
            arr[i+temp+1]=tempValue
            print(i)

        print(arr)  
            
x = ReArrangeArray()
x.ArrayData([12,23,44,55,1,2,4,5])