#!/usr/bin/env python

"""
Usage:
./diff_exp.py hema_data.txt
"""

import sys
import pandas as pd
from scipy.stats import ttest_ind, ttest_rel

def average_early_late( early, late ):
    data_df = pd.read_csv( sys.argv[1], sep='\t' )
    data_df['early_mean'] = data_df[ early ].mean( axis=1 )
    data_df['late_mean'] = data_df[ late ].mean( axis=1 )
    return data_df
    
def get_diff_stats( average_df, early, late ):
    average_df['ratio'] = average_df['early_mean'] / average_df['late_mean']
    stat, p = ttest_ind( average_df[early], average_df[late], axis=1 )
    average_df['p-value'] = p
    average_df = average_df.mask( average_df['p-value'] > 0.05 ).dropna(how='any')
    average_df = average_df.mask( average_df['ratio'] > 0.5 ).dropna(how='any')
    
    return average_df
    
def main():
    early = [ 'CFU', 'mys' ]
    late = [ 'poly', 'unk' ]
    averaged = average_early_late( early, late )
    avg_and_stats = get_diff_stats( averaged, early, late )
    
main()
        