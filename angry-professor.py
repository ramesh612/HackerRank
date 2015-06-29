#!/usr/bin/env python

def class_cancelled(arrival_times, min_students):
    ontime_count = sum([True for x in arrival_times if x <= 0])
    # print ontime_count, min_students
    if ontime_count < min_students:
        return "YES"
    else:
        return "NO"
    
n_lines = raw_input()

for _ in range(int(n_lines)):
    line1 = raw_input()
    n,min_students = map(int, line1.split())
    line2 = raw_input()
    arrival_times = map(int, line2.split())
    print class_cancelled(arrival_times, min_students)