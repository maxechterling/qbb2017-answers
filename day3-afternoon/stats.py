#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

total = 0.0
counts = 0.0

for line in f:
    total = total + float(line)
    counts += 1
    
print total / counts

f.close()
