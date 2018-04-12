#!/usr/bin/python3

import struct

# short int short short int (native, unsigned)
unpacker = struct.Struct('=HIHHI')

with open('../DATA/chimp.bmp','rb') as CHIMP:
    chimp_bmp = CHIMP.read()

(signature,size,reserved1,reserved2,offset) = unpacker.unpack(chimp_bmp[0:14])

print("signature:",signature)
print('size:',size)
print('reserved1:',reserved1)
print('reserved2:',reserved2)
print('offset:',offset)
