#!/usr/bin/env python

"""
query = droyak.fa
target = subset.fa
k = kmer length
./kmer_match.py <target.fa> <query.fa> <k>

OUTPUT
tab delimited
target_seq_name target_start query_start k-mer
"""

import sys
import fasta

#bring in files / arguments
target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])

#need a function to break a sequence into k-mers
def kmerSplit(seq, k):
    """
    Takes a sequence and breaks it into k-mers of length k. Returns dictionary of
    k-mers mapped to the positions (0-indexed) of those k-mers in the sequence.
    """
    kmer_dic = {}
    seq = seq.upper()
    for i in range( 0, len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in kmer_dic:
            kmer_dic[kmer] = [i]
        else:
            kmer_dic[kmer].append(i)
    return kmer_dic

#let's build the target_index
#{k-mer : [[sequence_name1, position1a, position1b],[sequence_name2, position2a, position2b]]}
target_index = {}

for ident, sequence in fasta.FASTAReader( target ):
    #entry = [ident]
    #print sequence
    kmers = kmerSplit(sequence, k)
    for key, value in kmers.items():
        if key not in target_index:
            target_index[key] = [[ident] + value]
            #print target_index[key]
        else:
            target_index[key].append([ident] + value)
            #print target_index[key]
            
#now we'll iterate through the query kmers and print outputs
q_ident, q_seq = fasta.FASTAReader(query).next()

for i in range( 0, len(q_seq) - k + 1):
    q_seq = q_seq.upper()
    kmer = q_seq[i:i+k]
    if kmer not in target_index:
        pass
    else:
        ind_data = target_index[kmer]
        for entry in ind_data:
            if len(entry) == 2:
                print '%s\t%s\t%s\t%s' % (entry[0], entry[1], i, kmer)
            else:
                for j in range(1, len(entry)):
                    print '%s\t%s\t%s\t%s' % (entry[0], entry[j], i, kmer)
                    

        
#target_seq_name target_start query_start k-mer
    
#test_seq1 = 'GCTGTTGTGGCCAGGATTTGGATTTGTTGTGCTGTGTTCTGCTCTGTTTTCTGTTCGGTGAGCTTTGCTGTGGACCAGAGTGCGCATTTGGTGTGGGTTTCGGTTTGGCTGGCTCCTTTGGCCAGCTGGAGGGCATTCCTCGCCATTCTC'          
#test_seq2 = 'GCTGCT'
#print kmerSplit(test_seq2, 3)

#ident, seq = fastaFASTAReader(query).next()
