#!/usr/bin/python3

def nextPrime(limit):
    flags = [False] * (limit+1)  # initialize flags

    for i in range(2,limit):
        if flags[i]:
            continue
        for j in range(2*i,limit+1,i):
            flags[j] = True
        yield i  # execution stops here until next value is requested by for-in loop

for p in nextPrime(100):
    print(p, end=' ')

