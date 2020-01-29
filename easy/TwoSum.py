# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:01:29 2020

@author: abasavar

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class TwoSum:
        
    def getData(self,nums,target:int):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]
       
def main():
    x=TwoSum()
    print(x.getData([4,4,6,7,8],8))
    
    
if __name__ == "__main__":
    main()