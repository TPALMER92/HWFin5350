#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:14:29 2017

@author: courtenaenielson
"""

import numpy as np
from scipy.stats import binom
import abc
import enum
from scipy.stats import norm

class PricingEngine(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        " " "
        " " "
        pass
    
#class VanillaOption(object):
    #def __init__(self, strike, expiry):
        #self.strike = strike
        #self.expiry = expiry
        
        #def payoff(self, spot) :
            #pass
        
#class VanillaCallOption(VanillaOption) :
    #def value(self, spot) :
        #return np.maximum(spot - self.strike, 0.0)
    
#class VanillaPutOption(VanillaOption) :
    #def value(self, spot) :
        #return np.maximum(self.strike - spot, 0.0)


def AmericanBinomialPricer(pricingengine, option, data) :
    (spot, rate, volatility, dividend) = data.get_data()
    expiry = option.expiry
    strike = option.strike
    steps = pricingengine.steps
    nodes= steps + 1
    spotT = np.zeros(nodes)
    callT = np.zeros(nodes)
    dt = expiry / steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt))
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp((rate - dividend) * dt) - d) / (u - d)
    pd = 1 - pu
    disc = np.exp(-rate * dt)
    dpu = disc * pu
    dpd = disc * pd
    #numnodes = self.steps + 1
    
    
    for i in range(nodes):
        spotT[i] = S * (u ** (steps - i)) * (d **(i))
        callT[i] = option.value(spotT[i])
        #tree[i, 3] = S * (u ** (N - i)) * (d ** i)
        #price = callT * np.exp(-rate * option.expiry)
    
    for i in range((steps-1),-1,-1):
        for j in range(i+1):
            callT[j] = dpu * callT[j] + dpd * callT[j+1]
            spotT[j] = spotT[j] / u 
            callT[j] = np.maximum(callT[j], option.value(spotT[j])
            #tree[j,i] = tree[j+1,i+1] / d
        
#S = 41.0
#K = 40.0
#r = 0.08
#v = 0.30
#div = 0.0
#T = 1.0
#N = 3
#dt = T / N
#nodes = N + 1
#tree = np.zeros((nodes, nodes))

#theCall = VanillaCallOption(K, T)
#callPrice = AmericanBinomialPricer(theCall, S, r, v, div, N)
#print(callPrice)

#thePut = VanillaPutOption(K, T)

#putPrice = AmericanBinomialPricer(thePut, S, r, v, div, N)
#print(putPrice)
    return callT[0]
