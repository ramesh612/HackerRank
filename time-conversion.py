#!/usr/bin/env python

# parse input
inp = raw_input()
am_pm = inp[-2:]
(hr,mi,ss) = map(int, inp[:-2].split(':'))

# assertions
assert (hr >= 1 and hr <= 12)
assert (mi >= 0 and mi <= 59)
assert (ss >= 0 and ss <= 59)

# logic
if (am_pm == "PM" and hr != 12) or (am_pm == "AM" and hr == 12):
    hr += 12
if hr == 24:
    hr = 0

# output
print "%02d:%02d:%02d" % (hr, mi, ss)
