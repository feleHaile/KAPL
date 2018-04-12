#!/usr/bin/env python
from functools import wraps

cache = {}

def kapl_cache(orig_function):

    @wraps(orig_function)
    def replacement(*args):
        if args not in cache:
            cache[args] = orig_function(*args)
        return cache[args]

# something like
#    wraps(replacement, orig_function)

    return replacement


@kapl_cache
def get_thing(a, b):
    print(f"params {a} {b}")
    return a ** b

# get_thing = kapl_cache(get_thing)

print(get_thing.__name__)

for x, y in (1, 3), (4, 5), (1, 3), (2, 8), (1, 3):
    print(get_thing(x, y))

#  @A
#  def B(): pass

#  B = A(B)

