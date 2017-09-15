#!/usr/bin/env python

"""
./realign.py <prot.fa> <nuc.fa> <output_figure>
"""

import sys
import fasta
import numpy as np
from statsmodels.stats.weightstats import ztest
import matplotlib.pyplot as plt

aa = open( sys.argv[1] )
nuc = open( sys.argv[2] )

aa_list = []
nuc_list = []

for ident, seq in fasta.FASTAReader( aa ):
    # Need * for stop codon
    aa_list.append( seq )

for ident, seq in fasta.FASTAReader( nuc ):
    # Split nuc_list into codons
    codons = []
    stop_cods = ['TAG', 'TAA', 'TGA']
    for i in range( 0, len(seq), 3 ):
        if seq[i:i+3] in stop_cods:
            pass
        else:
            codons.append( seq[i:i+3] )
    nuc_list.append( codons )

def realign( aa_seq, nuc_seq ):
    """
    takes a single aa sequence and unaligned nucleotide sequence. Returns nuc_seq aligned to the aa seq
    w/ triple dashes added at insertion sites.
    """
    for i in range(len(aa_seq)):
        if aa_seq[i] == '-':
            nuc_seq.insert(i, '---')
    return aa_seq, nuc_seq


# Realigned query sequences
q_aa, q_nuc = realign( aa_list[0], nuc_list[0] )
q_aa = q_aa.replace('*','')

# Storing lists of the [dS, dN] counts at each codon position
counts = [ [ 1, 1 ] for x in range( len(q_aa) ) ]

for i in range( 1, len(nuc_list) ):
    aa_seq, n_seq = realign( aa_list[i], nuc_list[i] )
    aa_seq = aa_seq.replace('*', '')
    for j in range( 0, len(aa_seq) ):
        # If no mutation occurs, pass
        if aa_seq[j] == q_aa[j] and n_seq[j] == q_nuc[j]:
            pass
        # If synonymous mutation occurs, +1 to dS
        elif aa_seq[j] == q_aa[j] and n_seq[j] != q_nuc[j]:
            counts[j][0] += 1
        # If non-synonymous mutation occurs, +1 to dN
        else:
            counts[j][1] += 1

diffs = []
labels = []
ratios = []
tot_counts = []
for i, aa in enumerate(q_aa):
    if aa == '-':
        pass
    else:
        diffs.append( counts[i][1] - counts[i][0])
        #counts[i] = [ 1 if x == 0 else x for x in counts[i] ]
        ratios.append( float(counts[i][1]) / float(counts[i][0]) )
        tot_counts.append( float(counts[i][0] + counts[i][1]))

#stdev = np.std( diffs )
#stderr = stdev / len(diffs)**.5
#stdev = np.std( ratios )
#stderr = stdev / len( ratios )**.5

t_test = []
sig = {}
insig = {}

# for i, samp in enumerate(diffs):
#     t = (samp - 0 ) / stderr
#     # p < 0.005
#     if t > 2.58:
#         sig[i] = ratios[i]
#     else:
#         insig[i] = ratios[i]

for i, samp in enumerate(diffs):
    stdev = np.std( diffs )
    stderr = stdev / tot_counts[i]**.5
    t = (samp - 0) / stderr
    # p < 0.005
    if t > 2.58:
        sig[i] = ratios[i]
    else:
        insig[i] = ratios[i]
#

plt.figure(figsize=(25,10))
#plt.scatter(x , ratios)
sig = plt.scatter(sig.keys(), np.log2(sig.values()), color='r', alpha=0.7, label='p < 0.005')
plt.scatter(insig.keys(), np.log2(insig.values()), color='gray', alpha=0.7)
#plt.hist(np.log2(insig.values()), bins=100)
plt.xlabel('codon position in query sequence', fontsize=15)
plt.ylabel('log2(dS/dN)', fontsize=15)
plt.title('Enrichment of synonymous mutations in a query sequence', fontsize='22')
plt.legend(handles=[sig],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.xlim(-30, 3450)
#plt.ylim(-6.5, 10.5)
plt.savefig( sys.argv[3] + '.png')
plt.close()