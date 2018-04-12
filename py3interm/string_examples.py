#!/usr/bin/env python

s1 = 'spam\n'
s2 = "spam\n"
s3 = '''spam\n'''
s4 = """spam\n"""
s5 = r'''spam\n'''
print("It's a beautiful day in the neighborhood")
print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print("""Guido's the "BDFL" of Python""")

name = 'Billy Rogers'
print(name[0], name[-1])
print(len(name))
print(name[:5])

print(name[0:3])
print(name[4:8])
print(name[-6:])

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


print(fruits[0:5])
print(fruits[:5])
print(fruits[8:13])
print(fruits[-3:])

foo = 'hello, world'   # sequence of characters
bar = b'hello world'  # sequence of bytes

print(foo.encode())
print(bar.decode())

print(foo[0], bar[0])
print(foo)
print(bar)

print(bar.upper())

print(foo.upper(), foo.lower(), foo.capitalize(), foo.title(), sep="|")

print(foo.index('hel'))
print(foo.find('kit'))

s = '   The mix is in the annex closet    '
print('|', s.lstrip(), '|')
print('|', s.rstrip(), '|')
print('|', s.strip(), '|')
print()

s = 'xssssxxxssxxxxxThe mix is in the annex closetsxsxsxsxsxxxsxsx'
print('|', s.lstrip('xs'), '|')
print('|', s.rstrip('xs'), '|')
print('|', s.strip('xs'), '|')
print()

print(name)
print(name.startswith('Bill'))
print(name.startswith('Beak'))
print('oz' in name)
print('og' in name)

x = 80
y = 27
result = 80 / 27

print("{} / {} is {}".format(x, y, result))
print("{} / {} is {:.2f}".format(x, y, result))
# 3.6+
print(f"{x} / {y} is {result:.2f}")

value1 = 1234
value2 = 3.98
print("{1:.5f} {0} {0:x} {0:b} {0:o} {0:05d} {1}".format(value1, value2))


big_num = 3209029834029384029384
print("{:,d}".format(big_num))

colors = ['red', 'blue', 'purple']
print('{0[0]} {0[2]}'.format(colors))

