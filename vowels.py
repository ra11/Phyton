# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:02:10 2023

@author: sathy
"""

i = input('Enter text: ')

for char in i:
    if char.lower() in 'aeiou':
        print(char)   
    