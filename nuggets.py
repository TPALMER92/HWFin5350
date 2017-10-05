#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:34:37 2017

@author: courtenaenielson
"""
def is_nugget_number(candidate, small=6, medium=9, large=20):
    for i in range(int(candidate/small + 1)):
        for j in range(int(candidate/medium + 1)):
            for k in range(int(candidate/large +1)):
                if(small*i + medium*j + large*k == candidate):
                    return True
    return False
            