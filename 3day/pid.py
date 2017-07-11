#!/usr/bin/env python
# -*- conding: utf-8 -*-
import sys
import string
import os

def  isNum(s):
    for i in s:
        if i in string.digits:
            continue
        else:
            return False
    return True

for pid in os.listdir('/proc'):
    if isNum(pid):
        print pid
        
