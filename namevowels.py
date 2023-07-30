# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:48:03 2023

@author: sathy
"""

input_string = input("Enter names: ")
name_list = input_string.split(" ")
for name in name_list:
 vowels = ('a', 'e', 'i', 'o', 'u');
 if any(char in vowels for char in name):
    print (name, "is a vowel.")
 else:
        print (name, "is not a vowel.")