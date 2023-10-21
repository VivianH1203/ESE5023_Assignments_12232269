#!/usr/bin/env python
# coding: utf-8

import numpy as np
def Matrix_multip(M1, M2):
    result = np.empty([5, 5])
    for ii in range(result.shape[0]):
        for jj in range(result.shape[1]):
            for kk in range(M1.shape[1]):
                result[ii,jj] += M1[ii,kk] * M2[kk,jj]
    return result

M1 = np.random.randint(0, 50, (5, 10))
M2 = np.random.randint(0, 50, (10, 5))
print(Matrix_multip(M1,M2))

