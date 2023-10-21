#!/usr/bin/env python
# coding: utf-8

def Find_expression(num):
    cal = ['+','-','']
    count = 0
    for n1 in cal:
        for n2 in cal:
            for n3 in cal:
                for n4 in cal:
                    for n5 in cal:
                        for n6 in cal:
                            for n7 in cal:
                                for n8 in cal:
                                    if eval('1%s2%s3%s4%s5%s6%s7%s8%s9'%(n1,n2,n3,n4,n5,n6,n7,n8)) == num:
                                        count += 1
    return count

Total_solutions = []
for ii in range(1,100):
    Total_solutions.append(Find_expression(ii))

import matplotlib.pyplot as plt
plt.plot(Total_solutions)

import numpy as np
maxval = max(Total_solutions)
print(maxval)
max_index = [i for i, value in enumerate(Total_solutions) if value == maxval]
print(np.array(max_index)+1)
minval = min(Total_solutions)
min_index = [i for i, value in enumerate(Total_solutions) if value == minval]
print(np.array(min_index)+1)