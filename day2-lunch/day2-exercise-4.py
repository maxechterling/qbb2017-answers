#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

count = 0
linecount = 0
chromos = []

for line in f:
    if line.startswith( "@" ):
        continue
    id = line.split('\t')
    if id[2] != '*':
        chromos.append(id[2])
    else:
        pass
    
print chromos[:10]