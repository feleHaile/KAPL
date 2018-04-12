#!/usr/bin/python3

def ni(num_knights,repeat_count,silly_word):
    print("We are the {0} knights who say {1}".format(num_knights,silly_word))
    for i in range(repeat_count):
        print(silly_word, end=' ')
    print()

values = ( 15, 5, 'ni!')

# tedious way
ni(values[0],values[1],values[2])

# pythonic way
ni(*values)
