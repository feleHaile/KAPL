#!/usr/bin/python3
from pyparsing import Word, alphas

# define grammar
greet = Word( alphas ) + "," + Word( alphas ) + "!"

# input string
hello = "Hello, World!"

# parse input string
print(hello, "->", greet.parseString( hello ) )