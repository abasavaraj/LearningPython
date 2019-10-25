#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:20:07 2019

@author: abasavaraj
"""
import json
import re

try:
    f = open("/Users/abasavaraj/Downloads/MS_sample.txt")
    g= f.read()
    temp=json.loads(g)
    for x,y in temp.items():
        if re.search("gassetsan",x):
            print(y)
        
        
except:
    print("Could not open the file")
finally:
    f.close()
    print("Close file connection")
