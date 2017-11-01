#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:16:05 2017

@author: courtenaenielson
"""

import numpy as np
from scipy.stats import binom

class VanillaOption(object):
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
        
        def payoff(self, spot) :
            pass
        
class VanillaCallOption(VanillaOption) :
    def value(self, spot) :
        return np.maximum(spot - self.strike, 0.0)
    
class VanillaPutOption(VanillaOption) :
    def value(self, spot) :
        return np.maximum(self.strike - spot, 0.0)


def EuropeanBinomialPricer(option, S, rate, volatility, dividend, steps) :
    nodes= steps + 1
    spotT = 0.0
    callT = 0.0
    dt = option.expiry / steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt))
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp((rate - dividend) * dt) - d) / (u - d)
    #pu = (np.exp((rate - option.expiry)*dt) - d) / (u - d)
    pd = 1 - pu
    
    for i in range(nodes):
        spotT = S * (u ** (steps - i)) * (d **(i))
        callT += option.value(spotT) * binom.pmf(steps - i, steps, pu)
    price = callT * np.exp(-rate * option.expiry)

    return price

S = 41.0
K = 40.0
r = 0.08
v = 0.30
div = 0.0
T = 1.0
N = 3


theCall = VanillaCallOption(K, T)
callPrice = EuropeanBinomialPricer(theCall, S, r, v, div, N)
print(callPrice)


thePut = VanillaPutOption(K, T)

putPrice = EuropeanBinomialPricer(thePut, S, r, v, div, N)
print(putPrice)




