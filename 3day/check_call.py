#!/usr/bin/env python3
# -*- conding: utf-8 -*-
import subprocess

try:
    subprocess.check_call('exit 1',shell=True)
except Exception :
    print('hello,world')
