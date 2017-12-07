#!/usr/bin/env python

"""
Usage:

./heatmapper.py abundance_table.tab

"""

import sys
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv( sys.argv[1], sep='\t', index_col=0 )

bin_dic = { 'bin.1': 'Staphylococcus haemolyticus', 'bin.2': 'Leuconostoc citreum', 'bin.3': 'Staphylococcus lugdenensis',\
            'bin.4': 'Enterococcus faecalis', 'bin.5': 'Cutibacterium avidum', 'bin.6': 'Staphylococcus epidermidis',\
            'bin.7': 'Staphylococcus aureus', 'bin.8': 'Anaerococcus prevotii' }

genomes = [ bin_dic[ bin ] for bin in data.index ]

def hierch_clustering( data_df_oi, labels ):
    flipped = np.transpose( data_df_oi.values )
    linkx, linky = linkage( data_df_oi.values, method='average' ), linkage( flipped, method='average' )
    leavesx, leavesy = leaves_list( linkx ), leaves_list( linky )
    transformed = data_df_oi.values[ leavesx,: ]
    labels_tr = np.array( labels )[leavesx]
    return transformed, labels_tr, linky, leavesy
    
def plot_heatmap( tr_intensities, ylabels, xlabels ):
    plt.figure()
    plt.imshow( tr_intensities, aspect='auto', interpolation='nearest') #, cmap='RdBu' )
    plt.grid( False )
    plt.colorbar( label='abundance' )
    plt.title( 'Genome Abundance Post-Birth' )
    plt.yticks( [ x for x in range( len( ylabels ))], ylabels )
    plt.xticks( [ x for x in range( len( xlabels ))], xlabels, rotation='vertical' )
    plt.tight_layout()
    plt.savefig( 'genome_abundance.png' )
    plt.close() 

tr, tr_genome_labels, linky, leavesy = hierch_clustering( data, genomes )
data_tr = pd.DataFrame( tr, columns=data.columns, index=tr_genome_labels )[['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]
stage_labels = data_tr.columns
plot_heatmap( data_tr, tr_genome_labels, stage_labels  )
    
