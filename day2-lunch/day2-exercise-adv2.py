#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

count = 0

for line in f:
    if line.startswith( "@" ):
        continue
    id = line.split('\t')
    if id[2] == '2L' and int(id[3]) >= 10000 and int(id[3]) <= 20000:
        count += 1
print count
    