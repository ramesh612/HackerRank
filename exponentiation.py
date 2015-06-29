#!/usr/bin/env python

def power(x,n):
    if n < 0: return power(1 / x, - n )
    elif n == 0: return  1
    elif n == 1: return  x
    elif n % 2 == 0: return power(x * x,  n / 2);
    elif n % 2 == 1: return x * power(x * x, (n - 1) / 2)

def power2(x, n):
    if n < 0:
      x = 1 / x
      n = -n
    if n == 0: return 1
    y = 1
    while n > 1:
      if n % 2 == 0: 
        x = x ** 2
        n = n / 2
      else:
        y = x * y
        x = x * x
        n = (n - 1) / 2
    return x * y
    
print pow (639624893, 451163041, 10**9+7)