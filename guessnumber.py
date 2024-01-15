# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:08:55 2023

@author: sathy
"""

print("I have number from 1-20")
# Initializing the number
n=12

#Taking Inputs
guess = int(input("Enter any number: "))

# Initializing the number of guesses.
count=3
# guesses depends upon range
for i in range(count):
   # Condition testing 
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    elif guess == n:
            print("Your correct!")
# If Guessing is more than required guesses,
# shows this output.               
print("You ran outo of attempts.The number was 12. Better Luck Next time!")
     
   
