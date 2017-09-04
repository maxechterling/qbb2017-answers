#!/usr/bin/env python

"""
Usage: ./hist_pred.py <ctab>
"""

import sys

import pandas as pd


#coi = [ 'chr', 'start', 'end', 't_name', 'strand' ]

df = pd.read_csv( sys.argv[1], sep='\t')

for index, row in df.iterrows():
    if row['strand'] == '+':
        start = row['start'] - 500
        if start < 0:
            start = 0
        end = row['start'] + 500
        print '%s\t%d\t%d\t%s' % (row['chr'], start, end, row['t_name'])
    else:
        start = row['end'] + 500
        end = row['end'] - 500
        if end < 0:
            end = 0
        print '%s\t%d\t%d\t%s' % (row['chr'], start, end, row['t_name'])

