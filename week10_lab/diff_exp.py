#!/usr/bin/env python

"""
Usage:
./diff_exp.py hema_data.txt
"""

import sys
import pandas as pd
from scipy.stats import ttest_ind, ttest_rel
from sklearn.cluster import KMeans

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
    
def k_means_clustering( X ):
    ## making way more clusters here than before to limit the number of genes in the panther output
    kmeans = KMeans( n_clusters=7, random_state=0 )
    kmeans.fit( X[['CFU','poly', 'unk', 'int', 'mys', 'mid']] )
    labels = kmeans.predict( X[['CFU','poly', 'unk', 'int', 'mys', 'mid']] )
    X = pd.merge( pd.DataFrame(X), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
    return X.sort_values('cluster')[[ 'CFU', 'poly', 'unk', 'int', 'mys', 'mid', 'cluster', 'gene' ]]
    
def main():
    ## I have no idea if these are actually the early and late cell types... just my best guess
    ## based on the dendrogram
    # early = [ 'CFU', 'mid', 'int' ]
    # late = [ 'poly', 'unk', 'mys' ]
    # early = [ 'CFU', 'int', 'mys' ]
    # late = [ 'poly', 'unk', 'mid' ]
    early = [ 'CFU', 'mys' ]
    late = [ 'poly', 'unk' ]
    averaged = average_early_late( early, late )
    avg_and_stats = get_diff_stats( averaged, early, late )
    print 'differentially regulated genes\n(p-value < 0.05, ratio > 2 or < 0.5)\n'
    print avg_and_stats.to_csv( index=False, sep='\t' )
    clustered = k_means_clustering( averaged )
    cluster_oi = int( clustered[clustered.gene=='Lgals9'].cluster.to_string( index=False ) )
    clustered_genes = clustered.mask( clustered['cluster'] != cluster_oi )
    print '\ngenes clustered with Map3k6 (k=30)\n'
    print ', '.join( clustered_genes.dropna()['gene'].values )

main()