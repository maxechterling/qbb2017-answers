#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

count = 0

for line in f:
    if line.startswith( "@" ):
        continue
    #id = line.split('\t')
    #print id[0]
    count += 1

print count

f.close()