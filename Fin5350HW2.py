#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:08:19 2017

@author: courtenaenielson
"""

import random

def print_header():
    print("let me guess your number")
    print("ill guess your number and you tell me if its too high or too low")
    print("i bet i can do it in 6 guesses or less")
    
def print_footer(tries):
    print("that was fun lets play again")
    print("it only took me", tries,"tries")
    
def main():
    print_header()
    low = 1
    high = 100
    guess = int((low+high)/2)
    found = False
    tries = 1
    while found == False:
        response = input("is it " + str(guess) + "? y/n:")
        if(low == high):
            print("liar!")
            break
        if response == 'y':
            print("i knew it!")
            found = True
        else:
            response = input("is it higher or lower than " + str(guess) + "? h/l:")
            if response == 'h':
                low = guess
                guess = int((low+high)/2)
            else:
                high = guess
                guess = int((low+high)/2)
                
            tries += 1
    print_footer(tries)
    
if __name__ == "__main__":
    main() 