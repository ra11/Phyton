# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:48:03 2023

@author: sathy
"""
"""a=[]
for name in range(5):
 input_string = input("Enter names: ")
 a.append(name)
 vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in vowels for char in  a):
       print (a, "is a vowel.")
else:
        print (a, "is not a vowel.")"""
        
a=[] 
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}   
for name in range(5):
    inputname=input("Enter name: ")
    a.append(inputname)
    
for name in a:
     if any(char in vowels for char in name):
        print (name, "is a vowel.")
     else:
         print (name, "is not a vowel.")