#!/usr/bin/env python3
# -*- conding: utf-8 -*-

def  is_old(n):
    return n % 2 == 1
print(list(filter(is_old,[1,2,3,4,5,6,7,8,9,10])))
