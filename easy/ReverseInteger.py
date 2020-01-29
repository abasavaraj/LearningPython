# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:16:09 2020

@author: abasavar

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class ReverseInteger:

    def reverse(self, x: int) -> int:
        revNumber=0
        r = range(-pow(2,31),pow(2,31)-1)
        isNegetive = False
        if (x not in r):
                return 0
        while (x !=0):
            if(x < 0):
                x = x * -1
                isNegetive = True
            y = x % 10
            revNumber = revNumber * 10 + y
            x = int((x/10))
        if (revNumber not in r):
                return 0
        elif(isNegetive):
            return revNumber * -1
        else:
            return revNumber
       
def main():
    x=ReverseInteger()
    print(x.reverse(1534236469))
    
    
if __name__ == "__main__":
    main()