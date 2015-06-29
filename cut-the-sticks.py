#!/usr/bin/env python

def cut(sticks_length):
    return [x-min(sticks_length) for x in sticks_length]

N = raw_input()
input = raw_input()
xs = input.split()
xs = map(int, xs)

while all(xs):
    xs = cut(xs)
    print len(xs)
    xs = [x for x in xs if x != 0]
    if xs == []:
        break
