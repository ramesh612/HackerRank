#!/usr/bin/env python

T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    # write code to compute answer
    q,r = divmod(A,B)
    answer += q
    while q >= C1:
        q,r = divmod(q,C1)
        answer += q
        q += r
    print answer