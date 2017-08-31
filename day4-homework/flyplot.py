#!/usr/bin/env python

"""
Usage: ./flyplot.py <samples.csv> <replicates.csv> <directory>
"""

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

transcript = 'FBtr0331261'

def read_to_list(soi, metadata):
    fpkms = []
    for sample in metadata['sample'][soi]:
        fname = os.path.join( sys.argv[3], sample, 't_data.ctab' )
        df = pd.read_csv( fname, sep='\t')
        roi = df['t_name'] == transcript
        fpkms.append(df[roi]['FPKM'].values[0])
    return fpkms
    
def make_replicate_df(sample, replicate):
    pass    

df_samples = pd.read_csv( sys.argv[1] )
df_replicates = pd.read_csv( sys.argv[2] )
labels = df_samples['stage'].values[:8]

soi_f = df_samples['sex'] == 'female'
soi_m = df_samples['sex'] == 'male'
soi_f_r = df_replicates['sex'] == 'female'
soi_m_r = df_replicates['sex'] == 'male'

fpkms_f = read_to_list(soi_f, df_samples)
fpkms_m = read_to_list(soi_m, df_samples)
#fpkms_f_r = fpkms_f[:4] + read_to_list(soi_f_r, df_replicates)
#fpkms_m_r = fpkms_m[:4] + read_to_list(soi_m_r, df_replicates)
fpkms_f_r = read_to_list(soi_f_r, df_replicates)
fpkms_m_r = read_to_list(soi_m_r, df_replicates)

plt.figure()
plt.plot(fpkms_f, label='female', color='blue')
plt.plot([4,5,6,7],fpkms_f_r, color='blue')
plt.plot(fpkms_m, color='g', label='male')
plt.plot([4,5,6,7],fpkms_m_r, color='g')
plt.xlabel('developmental stage')
plt.ylabel('mRNA abundance (FPKM)')
plt.title('Sxl', style='italic', fontsize='28')
plt.xticks(range(len(labels)), labels)
plt.legend(bbox_to_anchor=(1.15, 1), loc=2, borderaxespad=0.)
plt.savefig('timecourse.png', bbox_inches='tight')
plt.close()