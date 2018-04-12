#!/usr/bin/env python
# (c) 2016 John Strickler
#
import time

import pyximport
pyximport.install()
import cy_primes

import py_primes

timestamp = time.time()

prime_list = cy_primes.primes(10000)
print(prime_list[:10])

elapsed = time.time() - timestamp

print("cython took {:.3f} seconds to find {} primes".format(elapsed, len(prime_list)))
print()

timestamp = time.time()

prime_list = py_primes.primes(10000)
print(prime_list[:10])

elapsed = time.time() - timestamp

print("python took {:.3f} seconds to find {} primes".format(elapsed, len(prime_list)))
