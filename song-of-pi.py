#!/usr/bin/env python

pi = [int(ch) for ch in '31415926535897932384626433833']
for _ in range(int(raw_input())):
    candidate = [len(word) for word in raw_input().split()]
    if candidate == pi[0:len(candidate)]:
        print "It's a pi song."
    else:
        print "It's not a pi song."