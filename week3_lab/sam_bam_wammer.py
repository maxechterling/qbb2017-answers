#!/usr/bin/env python

"""
Takes a directory of fastq files, turns them into sam files with bwa mem, converts them to bam, sorts, and indexes them using samtools

Usage:
./sam_bam_wammer.py <fastq directory>
"""

import os
import sys

path =  os.path.abspath( sys.argv[1] )

files = os.listdir( path )

for each in files:
    prefix = each.split('.')[0]
    os.system( 'bwa mem -R "@RG\\tID:%s\\tSM:%s" sacCer3.fa variants_fastq/%s.fastq > %s.sam' % (prefix, prefix, prefix, prefix) )
    os.system( 'samtools view -b -S %s.sam > %s.bam' % (prefix, prefix) )
    os.system( 'samtools sort -m 100000000 %s.bam -o %s_sorted.bam' % (prefix, prefix) )
    os.system( 'samtools index %s_sorted.bam' % (prefix) )
    
    
# Freebayes command
# freebayes --fasta-reference reference/sacCer3.fa variants_bams/A01_09_sorted.bam variants_bams/A01_11_sorted.bam variants_bams/A01_23_sorted.bam variants_bams/A01_24_sorted.bam variants_bams/A01_27_sorted.bam variants_bams/A01_31_sorted.bam variants_bams/A01_35_sorted.bam variants_bams/A01_39_sorted.bam variants_bams/A01_62_sorted.bam variants_bams/A01_63_sorted.bam -= > var.vcf