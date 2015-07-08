#!/usr/bin/env python

import datetime

# parse input
(actual_day, actual_month, actual_year) = map(int, raw_input().split())
(expected_day, expected_month, expected_year) = map(int, raw_input().split())

# validate input
assert (actual_day >= 1 and actual_day <= 31)
assert (actual_month >= 1 and actual_month <= 12)
assert (actual_year >= 1 and actual_year <= 3000)

assert (expected_day >= 1 and expected_day <= 31)
assert (expected_month >= 1 and expected_month <= 12)
assert (expected_year >= 1 and expected_year <= 3000)

# logic

# form datetime.date objects
actual = datetime.date(actual_year, actual_month, actual_day)
expected = datetime.date(expected_year, expected_month, expected_day)

# compute the difference in days
delta_days = (actual-expected).days

# if the difference in days is <= 0, the book has been returned on or before the due date
if delta_days <= 0:
    hackos = 0
else:
    # when it is not returned on or before the due date , go in the order of year, month and days
    # to compute the fine
    if actual_year > expected_year:
        hackos = 10000
    elif actual_month > expected_month:
        hackos = (actual_month-expected_month) * 500
    else:
        hackos = delta_days * 15

# output
print hackos
    
