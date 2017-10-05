#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:15:56 2017

@author: courtenaenielson
"""

from nuggets import is_nugget_number

def main():
    small, medium, large = 6, 9, 20
    count = 0
    largest = small - 1
    candidate = small
    
    while count != small:
        if(is_nugget_number(candidate)):
            count += 1
        else:
            largest = candidate
            count = 0
        candidate += 1
            
    print("The largest number of nuggets you cannot buy is: " + str(largest))
    
if __name__ == "__main__":
    main()
    