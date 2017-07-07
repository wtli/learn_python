#!/usr/bin/env python3
# -*- conding: utf-8 -*-

def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end())
