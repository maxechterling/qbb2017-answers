#!/usr/bin/env python

"""
INSTRUCTIONS

flyParser2.py takes a single argument: the path to fly.txt downloaded from uniprot.org
Output must be redirected to a new file which will be used as input for flyMapper.py

e.g.
./flyParser2.py fly.txt > flyOutput
"""

import sys

f =  open( sys.argv[1] )

parsed = []

for line in f:
    if 'DROME' in line:
        split_line = line.split()
        start = len(split_line) - 2
        entry = split_line[start:]
        if 'FBgn' in entry[1]:
            parsed.append(entry)
        else:
            parsed.append([entry[1],'no entry']) 

for every in parsed:
    print every[0], every[1]