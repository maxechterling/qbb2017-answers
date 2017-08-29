#!/usr/bin/env python

import sys

fh = sys.stdin

for line in fh:
    if line.startswith( "t_id" ):
        continue
    fields = line.split('\t')
    print int(fields[4]) - int(fields[3])
    

fh.close()