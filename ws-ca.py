#!/usr/bin/python

from sys import stdin, stdout

from epics import ca
import time
import json

def onChanges(pvname = None, value = None, enum_strs = None, **kw):
    data = {}
    data['pvname'] = pvname
    data['value'] = value
    print json.dumps(data)
    stdout.flush()

# get stdin
# 'RNG:BEAM:CURR','RNG:BEAM:LIFE','RNG:ENG','RNG:OPER:MODE','RNG:OPER:STAT'
line = stdin.readline().strip()
pvlist = map(lambda x : x.strip("''"), line.split(','))

pvdict = {}
for pvitem in pvlist:
    # pvo = epics.PV(pvitem)
    # pvo.add_callback(onChanges)
    # pvdict[pvitem] = pvo
    chid = ca.create_channel(pvitem)
    eventID = ca.create_subscription(chid, callback=onChanges)

while True:
    pass

# mypv.clear_callbacks()
print 'Done'
