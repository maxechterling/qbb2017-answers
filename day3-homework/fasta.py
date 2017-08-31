#!/usr/bin/env python

"""
Parse every FASTA record from a file and print
"""

import sys

class FASTAReader(object):
    
    def __init__( self, input_file ):
        self.file = input_file
        self.last_ident = None
    
    def __iter__( self ):
        return self
        
    def next( self ):
        # verify it is a header line
        if self.last_ident is None:
            line = self.file.readline()
            assert line.startswith(">")
            ident = line.split()[0].lstrip(">")
        else:
            ident = self.last_ident
            
        seq = []

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith(">"):
                self.last_ident = line.split()[0][1:]
                break
            elif line == "":
                if seq:
                    return ident, "".join( seq )
                raise StopIteration
            else:
                seq.append(line)
                
        return ident, ''.join(seq)
