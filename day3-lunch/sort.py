#!/usr/bin/env python

import random

nums = [x for x in range(3, 100)]
print nums  

key = 14

checked = []
for i, n in enumerate(nums):
    checked.append([i, n])

while True:
    midInt = len(checked)/2 - 1
    mid = checked[midInt][1]
    if mid == key:
        print 'Found it at index %d!' % checked[midInt][0]
        break
    elif key > mid:
        checked = checked[mid:]
    elif key < mid:
        checked = checked[:mid]
    