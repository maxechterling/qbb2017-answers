#!/usr/bin/env python

"""
Usage:
./snp_hist.py <vcf> <output.png>
"""

import sys
import matplotlib.pyplot as plt

vcf = open( sys.argv[1] )

allele_freqs = []

for line in vcf:
    if line.startswith( '#' ):
        pass
    else:
        segs = line.rstrip('\r\n').split('\t')
        freqs = segs[7].split(';')[3].lstrip('AF=').split(',')
        for freq in freqs:
            allele_freqs.append(float(freq))

plt.figure()
plt.hist(allele_freqs, bins=20)
plt.xlabel( 'allele frequency' )
plt.ylabel( 'counts' )
plt.title( 'Allele frequencies from ten yeast segregant genomes' )
plt.savefig( sys.argv[2] )
plt.close()
# CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	A01_62	...

# GT:GQ:DP:AD:RO:QR:AO:QA:GL