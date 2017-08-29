#!/usr/bin/env python

import sys

f = open( sys.argv[1] )

count = 0

for line in f:
    if line.startswith( "@" ):
        continue
    id = line.split('\t')
    for each in id:
        if each.startswith( "NH" ) == True:
            NH = each
            if NH == 'NH:i:1\n':
                count += 1
            break
        else:
            pass

print count

f.close()
