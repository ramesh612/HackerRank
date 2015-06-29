#!/usr/bin/env python

import numpy

def h(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

# read and sort the input data
N = input()
K = input()
data = [input() for _ in range(0,N)]
data.sort()

# compute the diffs between successive values
diffs = [x-data[i-1] for i,x in enumerate(data) if i>0]
print diffs, h(diffs)
diffs_arr = numpy.array(diffs)

# find the indices of the min k-1 values among the diffs
indices = diffs_arr.argsort()[:K-1]

# find the values corresponding to the indices from input data
l = [[x-1,x] for x in indices]
matching_indices = list(set([item for sublist in l for item in sublist]))
values = map(lambda i: data[i+1], matching_indices)

print max(values) - min(values)


