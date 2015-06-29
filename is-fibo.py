#!/usr/bin/env python
import math

def is_perfect_square(n):
    m = int(math.sqrt(n))
    return n == m*m

def is_fibonacci(m):
    return is_perfect_square(5*m*m + 4) or is_perfect_square(5*m*m - 4);

for _ in range(int(raw_input())):
    if is_fibonacci(int(raw_input())):
        print "IsFibo"
    else:
        print "IsNotFibo"