#!/usr/bin/env python

"""
Usage:
./make_dot_plot.py <sorted_lastz.out> <output_graph.png>
"""

import sys
import matplotlib.pyplot as plt

l_count = 0
c_count = 0
plt.figure()
for line in open( sys.argv[1] ):
    l_count += 1
    if l_count == 1:
        pass
    else:
        line = line.rstrip('\r\n').split('\t')
        start, stop = int(line[0]), int(line[1])
        plt.plot( [start, stop], [c_count, c_count + abs(stop - start)] )
        c_count += abs(stop - start)

plt.xlim( 0, 100000 )
plt.ylim( 0, 100000 )
plt.xlabel( 'reference position' )
plt.ylabel( 'contig position' )
plt.title( sys.argv[2] )
plt.savefig( sys.argv[2].split('.')[0] )
plt.close()