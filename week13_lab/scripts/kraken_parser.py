#!/usr/bin/env python

"""

"""

import sys

input_dic = {}
with open( sys.argv[1] ) as f:
    for line in f:
        entry = line.rstrip('\r\n').split('\t')[1]
        if entry in set( input_dic.keys() ):
            input_dic[ entry ] += 1
        else:
            input_dic[ entry ] = 1
        
for key in input_dic.keys():
    print key
    print input_dic[key], '\t'.join( key.split(';') )