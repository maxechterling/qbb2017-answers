#!/usr/bin/env python

"""
Usage: ./dual_plot.py <ctab1> <ctab2>
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

coi = ['t_name', 'FPKM']

df893 = pd.read_csv( sys.argv[1], sep="\t" )[coi]
df915 = pd.read_csv( sys.argv[2], sep="\t" )[coi]
df_m = pd.merge( df893 , df915, on='t_name')

fit = np.polyfit(df_m['FPKM_x'], df_m['FPKM_y'], 1)
x = [x for x in range(0, 10000)]
y = [fit[0]*i + fit[1] for i in range(0,10000)]

plt.figure()
plt.scatter( df_m['FPKM_x'], df_m['FPKM_y'], alpha=0.4)
plt.xscale('symlog')
plt.yscale('symlog')
plt.xlabel('SRR072893 FPKM')
plt.ylabel('SRR072915 FPKM')
plt.title('FPKM for transcripts in SRR072893 vs SRR072915')
plt.xlim(0, 10000)
plt.ylim(0, 10000)
plt.plot(x, y, color='g')
plt.savefig( sys.argv[3] + '.png')
plt.close()
