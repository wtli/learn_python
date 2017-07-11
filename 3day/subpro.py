#!/usr/bin/env python
# -*- conding: utf-8 -*-
from subprocess import Popen, PIPE
p = Popen(['./test.sh'],shell=True)
p.wait()
print "main process"
