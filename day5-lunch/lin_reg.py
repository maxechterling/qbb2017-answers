#!/usr/bin/env python

"""
Usage: ./lin_reg.py <hist.tab directory> <ctab>
"""

import sys
import pandas as pd
import numpy as np
import os 
import statsmodels.api as sm

def get_files( dir ):
    """
    Takes a directory containing output .tab files, returns list of all .tab files within.
    """
    d_list = []
    d = os.listdir( dir )
    for line in d:
        if line.split('.')[1] == 'tab':
            d_list.append(line)
        else:
            pass
    return d_list
    
def get_dat_data( hist_tab ):
    """
    takes either a single hist_bed.tab file or a list of files. Returns a list of mean coverage for the given
    histone marker and a list of FPKM measurements associated with that coverage. If you pass it a list
    of .tab files instead it will return a list of lists containing mean histone coverage for each marker.
    """
    name_list = ['t_name','size','covered','sum','mean0','mean']
    fpkm_df = pd.read_csv( sys.argv[2], sep='\t' ).sort_values('t_name')
    fpkm_list = fpkm_df['FPKM'].values
    hist_list = []
    if type( hist_tab ) is list:
        for hist in hist_tab:
            hist_path = os.path.join( sys.argv[1], hist )
            hist_df = pd.read_csv( hist_path, sep='\t', names=name_list ).sort_values('t_name')
            hist_list.append( list(hist_df[ 'mean' ].values) )
        # convert from list of columns to list of rows. Need it in this format for OLS.
        hist_list = np.array(hist_list).transpose()
    else:
        hist_path = os.path.join( sys.argv[1], hist_tab )
        hist_df = pd.read_csv( hist_path, sep='\t', names=name_list ).sort_values('t_name')
        hist_list = list( hist_df[ 'mean' ].values )
    return hist_list, fpkm_list

def lin_fit( hist_bed ):
    """
    Takes a list with mean histone coverage for a given marker or a np array combining lists for all histone markers.
    Outputs linear regression report for each histone marker (marker.out) and for the combo of all markers (combined.out)
    """
    hist_list, fpkm_list = get_dat_data( hist_bed )
    hist_list_c = sm.add_constant(hist_list)
    results = sm.OLS(fpkm_list, hist_list_c).fit()
    if type(hist_list) is list:
        output = open(hist_bed.split('.')[0] + '.out', 'w')
    else:
        output = open('combined.out', 'w')
    output.write( str(results.summary()) )
    output.close()
    return

def __main__():
    hist_test = get_files( sys.argv[1] )
    lin_fit( hist_test )
    for marker in hist_test:
        lin_fit( marker )

__main__()
