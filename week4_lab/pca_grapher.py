#!/usr/bin/env python

"""
Usage:
./pca_grapher.py <plink.eigenvec> <out_plot.png>
"""

import sys
import matplotlib.pyplot as plt

x, y = [], []
for line in open( sys.argv[1] ):
    PCs = line.rstrip('\n').split(' ')
    x.append( float(PCs[2]) )
    y.append( float(PCs[3]) )

plt.figure()
plt.scatter( x, y )
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Principle Component Analysis')
plt.savefig( sys.argv[2] )
plt.close()
    