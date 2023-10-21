#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def Print_values(a,b,c):
    if a > b:
        if b > c:
            print(a,b,c)
        elif a > c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif b > c:
        if a > c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)
    return

Print_values(3,2,4)
Print_values(2,4,2)
Print_values(5,1,1)
Print_values(2,3,5)
