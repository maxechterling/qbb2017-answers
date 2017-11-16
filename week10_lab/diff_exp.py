#!/usr/bin/env python

"""
Usage:
./diff_exp.py hema_data.txt
"""

import sys
import pandas as pd
from scipy.stats import ttest_ind, ttest_rel

def average_early_late( early, late ):
    data_df = pd.read_csv( sys.argv[1], sep='\t' ).dropna(how='any')
    data_df['early_mean'] = data_df[ early ].mean( axis=1 )
    data_df['late_mean'] = data_df[ late ].mean( axis=1 )
    return data_df.dropna()
    
def get_diff_stats( average_df, early, late ):
    average_df['ratio'] = average_df['early_mean'] / average_df['late_mean']
    stat, p = ttest_ind( average_df[early], average_df[late], axis=1 )
    average_df['p-value'] = p
    average_df = average_df.dropna()
    average_df = average_df.mask( average_df['p-value'] > 0.05 ).dropna()
    down_df = average_df.mask( average_df['ratio'] > 0.5 ).dropna()
    up_df = average_df.mask( average_df['ratio'] < 2.0 ).dropna()
    return pd.concat( [ down_df, up_df ] )[['gene','ratio','p-value']].sort_values('p-value')
    
def main():
    ## I have no idea if these are actually the early and late cell types...
    early = [ 'CFU', 'mys', 'mid' ]
    late = [ 'poly', 'unk', 'int' ]
    averaged = average_early_late( early, late )
    avg_and_stats = get_diff_stats( averaged, early, late )
    print avg_and_stats.to_csv( index=False, sep='\t' )

main()