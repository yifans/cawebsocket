#!/usr/bin/python

from sys import stdin, stdout
from epics import PV

import time
import json

# get stdin
# e.g. 'RNG:BEAM:CURR','RNG:BEAM:LIFE','RNG:ENG','RNG:OPER:MODE','RNG:OPER:STAT'
line = stdin.readline().strip()
pvlist = map(lambda x : x.strip("''"), line.split(','))

pvdict = {}
for pvitem in pvlist:
    p = PV(pvitem)
    pvdict[pvitem] = p

time.sleep(0.5) # 如果不sleep，第一次循环某个pv返回的type是unknown
while True:
    for key in pvdict:
        pv = pvdict[key]
        data = {}
        data['pvname'] = key
        if pv.type == 'time_enum':
            data['value'] = pv.enum_strs[pv.value]
        elif isinstance(pv.value, float):
            data['value'] = str(round(pv.value,2))
        else:
            data['value'] = str(pv.value)
        if pv.units:
            data['value'] += ' '
            data['value'] += pv.units
        print json.dumps(data)
        stdout.flush()
    time.sleep(10)
