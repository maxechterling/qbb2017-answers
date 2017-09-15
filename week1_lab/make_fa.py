#!/usr/bin/env python

"""
./make_fa.py alignment.tsv
"""

import sys

f = open( sys.argv[1] )

for line in f:
    line = line.rstrip('\r\n').split('\t')
    seq = line[1].replace('-','')
    label = '>%s\n%s' % (line[0], seq)
    print label