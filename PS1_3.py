#!/usr/bin/env python
# coding: utf-8

import numpy as np
def Pascal_triangle(k):
    for ii in range(1, k + 1):
        if ii <= 2:
            print(np.ones(ii))
            result = np.ones(ii)
        if ii > 2:
            newresult = np.ones(ii)
            for jj in range(1, ii-1):
                newresult[jj] = result[jj-1] + result[jj]
            print(newresult)
            result = newresult