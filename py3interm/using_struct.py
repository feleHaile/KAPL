#!/usr/bin/env python
from struct import Struct


s = Struct('IffidhB5s')

print(s.size)

data = s.pack(3930203, 1.23, 99.88, 1234,
              4.3e33, 123, 5, '100\u00B0'.encode())

print(data)

values = s.unpack(data)

print(values)
print(values[-1].decode())

bitflag = values[6]
print('{:08b}'.format(bitflag))

mask = 0b00000100  # 00000100 0x00000100


print(bitflag & mask)
