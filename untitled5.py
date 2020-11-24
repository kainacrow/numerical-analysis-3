#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:32:29 2018

@author: Kaina
"""

N = 128

import numpy as np

def calculateError(tArray, xArray):
    e = 0.0
    for i in range(len(tArray)):
        if(np.abs(tArray[i] - xArray[i]) >e):
            e = np.abs(tArray[i]-xArray[i])
    return e


true_Cs = [] ## 8193 * 2
current_Cs = [] ## N+1 *2
subset_of_true_Cs = []
for i in range(8193):
    if i % (8192/N) == 0:
        subset_of_true_Cs.append(true_Cs[i:])
    
    
    
    
    
t0 = np.pi
tValues = list(np.arange(0.0, np.pi*2.0, 0.01))
Nlist = [1000]
errorList = []
errorListL2 = []
tValues.append(2*np.pi)