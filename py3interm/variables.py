#!/usr/bin/env python

name = 'Fred'   # create str obj and name it 'name'
value = 12   # create int obj and name it 'value'
nums = [1, 2, 5, 19] # create list obj...

#   'x' ----------->  ______
#   'value' ------->  | 12 |
#                     ------
#                       int
x = value
value = 99

things = nums
things.append(42)
print(things)
print(nums)
blech = list(things)
burb = things[:]
for t in nums, things, blech, burb:
    print(id(t))
print(nums == things)
print(nums == blech)
print(nums is things)
print(nums is blech)

value = 'wombat'
value = 4.2
value = True
value = None

# numeric
# int float bool complex

# char
# str bytes

# array-like
# list tuple

# mapping
# dict set frozenset

x = '123'

print(x * 5)
print(int(x) * 5)
print(float(x) * 5)

value = 1234
print(str(value))
print(float(value))
print(bool(value))

word = 'DeadBeef'
print(int(word, 16))

print(int('100010101', 2))

print(int('2938734element', 31))

#  str bytes list tuple





