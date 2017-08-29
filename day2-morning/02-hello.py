#!/usr/bin/env python

import sys

print "Hello", sys.argv[1]
print "{1} Hello {0}".format(sys.argv[1], "hey!")

print sys.argv
