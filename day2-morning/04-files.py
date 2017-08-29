#!/usr/bin/env python
import sys

print sys.argv

if len( sys.argv ) > 1:
    f = open( sys.argv[1] )
    first_line = f.readline()
    f.close()

else:
    first_line = sys.stdin.readline()

print first_line