#!/usr/bin/env python

"""
Usage:
./ctcf_itxn.py <ctcf_peaks.tsv> <Nora_Primers.bed>
"""

import numpy as np
import sys

def load_hifive_data():
    data = np.load( 'nora_enr.heat.npz' )
    return data[ '0.forward' ], data[ '0.reverse' ], data[ '0.enrichment' ]

def ctcf_binding():
    ctcf_sites = []
    for line in open( sys.argv[1] ):
        line = line.rstrip('\r\n').split( '\t' )
        if line[0] == 'chrX':
            ctcf_sites.append( line[1] )
    return ctcf_sites
    
def get_primer_dic():
    primer_dic = {}
    for line in open( sys.argv[2] ):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == '#chr':
            pass
        else:
            primer_dic[ line[1] + '_' + line[2] ] = line[3]
    return primer_dic

def ctcf_indices( primers, ctcf_sites ):
    ind = []
    for i, each in enumerate( primers ):
        start, stop = int( each[0] ), int( each[1] )
        for site in ctcf_sites:
            if int( site ) >= start and int( site ) <= stop:
                ind.append( i )
                break
    return ind

def ixn_pairs( fwd_ind, rev_ind, enr ):
    pairs = []
    for fwd in fwd_ind:
        top_rev, top = None, 0.
        for rev in rev_ind:
            if float( enr[ fwd ][ rev ] ) > top:
                top_rev = rev
                top = float( enr[ fwd ][ rev ] )
        pairs.append( ( fwd, top_rev ) )
    return pairs

def name_ixns( fwd, rev, pairs, primer_dic ):
    for ixn in pairs:
        fw_key = str( fwd[ ixn[0] ][0] ) + '_' + str( fwd[ ixn[0] ][1] )
        rv_key = str( rev[ ixn[1] ][0] ) + '_' + str( rev[ ixn[1] ][1] )
        print '%s\t%s' % ( primer_dic[ fw_key ], primer_dic[ rv_key ] )

def main():
    ## load in all data
    ctcf_sites = ctcf_binding()
    fwd, rev, enr = load_hifive_data()
    primer_dic = get_primer_dic()
    ## get indices of ctcf binding sites in hifive data
    fwd_ind, rev_ind = ctcf_indices( fwd, ctcf_sites ), ctcf_indices( rev, ctcf_sites )
    ## find top interacting ctcf pairs
    pairs = ixn_pairs( fwd_ind, rev_ind, enr )
    ## map top interactions to primer names
    name_ixns(fwd, rev, pairs, primer_dic )
        
main()

