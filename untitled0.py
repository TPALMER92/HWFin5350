#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:04:38 2017

@author: courtenaenielson
"""

import numpy as np
from scipy.stats import binom

def CallPayOff(Spot, Strike):
    return np.maximum(Spot - Strike, 0.0)

def EuropeanBinomial(S, X, r, u, d, T):
    numSteps = 2
    numNodes = numSteps + 1
    spotT = 0.0
    callT = 0.0
    pu = (np.exp(r*T)- d)/ (u-d)
    pd = 1 - pu
    
    for i in range(numNodes):
        spotT = S * (u ** (numSteps - i)) * (d ** (i))
        callT += CallPayOff(spotT, X) * binom.pmf(numSteps - i, numSteps, pu)
    callPrice = callT * np.exp(-r * T)

    return callPrice

def main():
    S = 41
    X = 40
    r = 0.08
    T = 1.0
    v = 0.30
    u = 1.2
    d = 0.8
    
    callPrice = EuropeanBinomial(S, X, r, u, d, T)
    print("The Two Period European Binomial Price is = {0:.4f}").format(callPrice)

main()
    