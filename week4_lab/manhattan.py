#!/usr/bin/env python

"""
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

path =  os.path.abspath( sys.argv[1] )
files = os.listdir( path )
    
def get_dat_data( file ):
    sig_x, sig_y, bad_x, bad_y = [], [], [], []
    count = 0
    for line in open( file ):
        if 'SNP' in line or 'NA' in line:
            pass
        else:
            cutoff = -np.log( .00005 )
            line = line.rstrip('\r\n').split()
            count += 1
            p = -np.log(float(line[8]))
            if p > cutoff:
                sig_x.append( count )
                sig_y.append( p )
            else:
                bad_x.append( count )
                bad_y.append( p )
                
    return sig_x, sig_y, bad_x, bad_y
    
def graph_dat_data( sig_x, sig_y, bad_x, bad_y, name ):
    plt.figure()
    plt.scatter(sig_x, sig_y, color='red', alpha=0.6, label='p < 0.00005')
    plt.scatter(bad_x, bad_y, color='turquoise', alpha=0.6, label='p > 0.00005')
    plt.ylabel('-log10(p-value)')
    plt.xlabel('SNP')
    plt.title(name)
    plt.legend()
    plt.savefig( name + '.png')
    plt.close()

for line in open( sys.argv[2] ):
    labels = line.split()
    break

for i in range(len(files)):
    path_name = './gwas/' + files[i]
    sig_x, sig_y, bad_x, bad_y = get_dat_data( path_name )
    graph_dat_data( sig_x, sig_y, bad_x, bad_y, labels[i] )