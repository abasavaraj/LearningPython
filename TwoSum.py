#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:12:23 2019

@author: abasavaraj
"""

#Runtime 792ms Memory 14.7MB
class Solution1:
    def twosum(nums,target):
        nums=nums
        target=target
        for x in range(len(nums)): 
            numTarget = target - nums[x]
            if numTarget in nums:
                if(nums.count(numTarget) > 1):
                    for y in range(len(nums)):
                        if(numTarget == nums[y] and y!= x):
                            return([x,y])
                elif(x != nums.index(numTarget)):
                    return([x,nums.index(numTarget)])
     
# Runtime 4488ms Memory 14.6MB    
class Solution2:
    def twosum(nums,target):
        nums=nums
        target=target
        for x in range(len(nums)): 
            numTarget = target - nums[x]
            for y in range(len(nums)):
                if(numTarget == nums[y] and y!= x):
                    return([x,y])

# Runtime 60ms Memory 15.2MB

class Solution3:
    def twosum(nums,target):
        nums=nums
        target=target
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
                print(dict)
            else:
                return [dict[target-nums[i]],i]


k = Solution3.twosum([3,2,5,6,7,4],6)
print(k)