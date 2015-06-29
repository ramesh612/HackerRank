#!/usr/bin/env python

for _ in range(int(raw_input())):
    number = raw_input()
    digits = [int(c) for c in number]
    print sum([True for d in digits if d != 0 and int(number) % d == 0])