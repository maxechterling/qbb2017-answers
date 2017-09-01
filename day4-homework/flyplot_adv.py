#!/usr/bin/env python

"""
Usage: ./flyplot.py <samples.csv> <directory> <gene_name>

Example output run w/ gene_name='Sxl'
"""

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#test_gene = Tim17b

def get_all_transcripts(gene_name, ctab_df):
    toi = ctab_df[ 'gene_name' ] == gene_name
    return np.average(ctab_df[toi]['FPKM'].values)
    
def read_to_list(soi, metadata):
    fpkms = []
    for sample in metadata['sample'][soi]:
        fname = os.path.join( sys.argv[2], sample, 't_data.ctab' )
        df = pd.read_csv( fname, sep='\t')
        #get_all_transcripts( sys.argv[3], df )
        #roi = df['t_name'] == transcript
        fpkms.append(get_all_transcripts( sys.argv[3], df))
    return fpkms

df_samples = pd.read_csv( sys.argv[1] )

labels = df_samples['stage'].values[:8]

soi_f = df_samples['sex'] == 'female'
soi_m = df_samples['sex'] == 'male'

fpkms_f = read_to_list(soi_f, df_samples)
fpkms_m = read_to_list(soi_m, df_samples)

plt.figure()
plt.plot(fpkms_f, label='female', color='blue')
plt.plot(fpkms_m, color='g', label='male')
plt.xlabel('developmental stage')
plt.ylabel('mRNA abundance (FPKM)')
plt.title( sys.argv[3], style='italic', fontsize='28')
plt.xticks(range(len(labels)), labels)
plt.legend(bbox_to_anchor=(1.15, 1), loc=2, borderaxespad=0.)
plt.savefig('timecourse_adv.png', bbox_inches='tight')
plt.close()