#!/usr/bin/env python
# -*- conding: utf-8 -*-
class FuncError(Exception):
    def __str__(self):
        return "I am func Error"

def fun():
    raise FuncError()

try:
    fun()
except FuncError,e:
    print e

try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass
