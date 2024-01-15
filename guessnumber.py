# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:08:55 2023

@author: sathy
"""

print("I have number from 1-20")
n=12
guess = int(input("Enter any number: "))
count=3
for i in range(count):
    
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    elif guess == n:
            print("Your correct!")
                
print("You ran outo of attempts.The number was 12. Better Luck Next time!")
     
   