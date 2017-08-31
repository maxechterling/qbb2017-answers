#!/usr/bin/env python

"""
Takes output from kmer-match.py and returns full k-mer matches sorted by length

./kmer-match-extender.py <kmer-match.out> <target.fa> <query.fa>
"""

import sys
import fasta
from operator import itemgetter

# read in output file from kmer-match.py and subset.fa
kmer_out = open( sys.argv[1] )
target_fa = open( sys.argv[2] )
query_fa = open( sys.argv[3] )

# make query seq string
q_ident, q_seq = fasta.FASTAReader(query_fa).next()

# make dictionary of target file
targ_dic = {}
for ident, sequence in fasta.FASTAReader( target_fa ):
    targ_dic[ident] = sequence

pre_sort = []

for line in kmer_out:
    line_in = line.rstrip('\r\n').split('\t')
    tar_start = int(line_in[1])
    q_start = int(line_in[2])
    tar_seq = targ_dic[line_in[0]].upper().split()[0]
    full_match = [tar_seq[tar_start]]
    # scan forward
    fc = 1
    while True:
        if tar_seq[tar_start + fc] == q_seq[q_start + fc]:
            full_match.append(q_seq[q_start + fc])
            fc += 1
        else:
            break
    # scan backwards
    rc = 1
    while True:
        if tar_seq[tar_start - rc] == q_seq[q_start - rc]:
            full_match[:0] = q_seq[q_start - rc]
            rc += 1
        else:
            break
    line_in.append(''.join(full_match))
    line_in.append(len(line_in[4]))
    pre_sort.append(line_in)

post_sort = sorted(pre_sort, key=itemgetter(5), reverse=True)

for line in post_sort:
    print '\t'.join(line[:5])