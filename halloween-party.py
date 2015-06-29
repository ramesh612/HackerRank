#!/usr/bin/env python

for _ in range(int(raw_input())):
    n = int(raw_input())
    if n % 2 == 0:
        print (n/2)**2
    else:
        print ((n**2)-1)/4