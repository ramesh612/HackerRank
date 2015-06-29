#!/usr/bin/env python

import string

elements = set()
s = raw_input()
for ch in s:
    # print ch
    if ch != ' ':
        elements.add(string.lower(ch))
        if len(elements) == 26:
            print "pangram"
            break

if len(elements) != 26:
    print "not pangram"