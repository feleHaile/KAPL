#!/usr/bin/env python

def get_message():
    return "Hello, world"

def print_message():
    message = get_message()
    print(message)

print_message()

def all_params(p1, p2=1234, *p3, p4, p5='wombat', **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print('=' * 10)

all_params('red', 'blue', p4='green', p5='purple')
all_params('red', p4='pink')
all_params(p2=100, p1=42, p5='wildebeest', p4=7)
all_params(5, 10, 15, 20, 25, p4=30, p5=35,
           file_name='ham.txt', animal='wombat')

def generic(*args, **kwargs):
    pass

generic()
generic(1, 2)
generic(1, 2, spam=3, eggs=4)
