#!/usr/bin/env python

import math

def partition(n):
	m = n
	xs = [0]
	i = 1
	while sum(xs) < n:
		xs.append(i)
		n -= (i ** 2)
		i += 1
	xs.append(m - sum(xs))
	print m, xs
	return xs

for i in range(100):
	assert i == sum(partition(i)), i
