#!/usr/bin/env python

import sys
import string

n = int(raw_input())
s = raw_input()
k = int(raw_input())

assert n >= 1 and n <= 100
assert k >= 0 and k <= 100
assert len(s) == n

def cipher(ch, k, max):
    k %= 26
    if ord(ch) + k > max:
        out = ord(ch) + k - 26
    else:
        out = ord(ch) + k
    return chr(out)

for ch in s:
    if ch in string.ascii_lowercase:
        sys.stdout.write(cipher(ch, k, 122))
    elif ch in string.ascii_uppercase:
        sys.stdout.write(cipher(ch, k, 90))
    else:
        sys.stdout.write(ch)
