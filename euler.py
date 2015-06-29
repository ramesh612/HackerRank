#!/usr/bin/env python

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

# primesM = lambda ns, m, limit: [k for k in map(lambda n: n ** m, ns) if k < limit]

def primesM(ns, m, limit):
    res = []
    for n in ns:
        val = n ** m
        if val < limit:
            res.append(val)
    return res

for _ in range(int(raw_input())):
    res = 0
    limit = int(raw_input())
    primes = sundaram3(limit)
    # print primes
    primes2 = primesM(primes, 2, limit)
    # print primes2
    primes3 = primesM(primes, 3, limit)
    # print primes3
    primes4 = primesM(primes, 4, limit)
    # print primes4
    # print primes, primes2, primes3, primes4
    for i in range(len(primes2)):
        for j in range(len(primes3)):
            for k in range(len(primes4)):
                # print i, j, k
                sum = primes2[i] + primes3[j] + primes4[k]
                if sum > limit:
                    break
                else:
                    # print sum
                    res += 1
    print res