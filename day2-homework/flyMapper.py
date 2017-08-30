#!/usr/bin/env python

"""
INSTRUCTIONS

flyMapper.py requires at least two arguments: the output file made from flyParser2 and a ctab file.
By default flyMapper will print 'NO MATCH' after non-matches (example output is yesPrint.out).
If a third argument is passed then non-matches will be skipped (example output is noPrint.out). 
By my convention make the third argument 'less' but any third argument will skip non-matches.

e.g.
./flyMapper.py <flyOutput> <ctab> [less]
"""

import sys

# uni_data is fly.txt parsed by flyMapper.py, t_data is the t_data.ctab file
uni_data =  open( sys.argv[1] )
t_data = open( sys.argv[2] )

# Make dictionary. keys = flybase ID, values = uniProt ID
uni_dict = {}
for line in uni_data:
    splitLine = line.rstrip('\r\n').split()
    uni_dict[splitLine[1]] = splitLine[0]

# loop through t_data and check for matches in uni_dict. 
for tran in t_data:
    tranSplit = tran.rstrip('\r\n').split()
    flyID = tranSplit[8]
    if flyID in uni_dict:
        tranSplit.append(uni_dict[flyID])
        print '\t'.join(tranSplit)
    # By default non-matched lines will print and say 'NO MATCH'
    # If ANY additional argument is passed to the script then non-matches will be skipped
    else:
        if len(sys.argv) > 3:
            pass
        else:
            tranSplit.append('NO MATCH')
            print '\t'.join(tranSplit)
        