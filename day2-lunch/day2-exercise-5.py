#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

total = 0
count = 0

for line in f:
    if line.startswith( "@" ):
        continue
    id = line.split('\t')
    total = total + float(id[4])
    count += 1

print total / float(count)
    