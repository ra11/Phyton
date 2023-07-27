# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:48:06 2023

@author: sathy
"""

for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        
	