#!/usr/bin/env python3
# -*- conding: utf-8 -*-

from functools import reduce

def add(x,y):
    return x + y

r=reduce(add,[1,2,3,4,5,6,7,8,9])
print(r)
