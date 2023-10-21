#!/usr/bin/env python
# coding: utf-8

def Least_moves(integer):
    count = 0
    while integer > 1:
        if integer % 2 == 0:
            count += 1
            integer = integer / 2
            print(count, integer)
        else:
            count += 1
            integer = integer - 1
            print(count, integer)
    return count

