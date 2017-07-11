#!/usr/bin/env python
# -*- conding: utf-8 -*-


from subprocess import Popen, PIPE

p = Popen(['dmidecode'],stdout=PIPE)
data = p.stdout
lines = []
dmi = {}
a = True
while a:
    line = data.readline()
    if line.startswith('System Information'):
        while  True:
            line = data.readline()
            if line == '\n':
                a = False
                break
            else:
                lines.append(line)
dmi_dic = dict([i.strip().split(':') for i in lines])
dmi['Manufacturer'] = dmi_dic['Manufacturer'].strip()
dmi['Product Name'] = dmi_dic['Product Name'].strip()
dmi['Serial Number'] = dmi_dic['Serial Number'].strip()

print(dmi)
