#!/usr/bin/env python

"""
./contigs_analyzer.py <contig.fa> <assembler_name>
"""

import fasta
import sys
import operator

total_l = 0
contigs = []
for name, seq in fasta.FASTAReader( open( sys.argv[1] )):
    if len(seq) == 0:
        pass
    sub = [name, seq, len(seq)]
    total_l += len(seq)
    contigs.append(sub)

contigs = sorted(contigs, key=operator.itemgetter(2), reverse=True)

print sys.argv[2]
print 'num contigs = %d' % ( len(contigs) )
print 'max contig length = %d' % ( contigs[0][2] )
print 'min contig length = %d' % ( contigs[-1][2] )
print 'avg contig length = %f' % ( float(total_l) / float(len(contigs)))

ldiv = float(total_l) / 2.0

tot = 0
for each in contigs:
    tot += each[2]
    if tot >= ldiv:
        n50 = each[2]
        break

print 'N50 = %d' % ( n50 )
print '\n'
