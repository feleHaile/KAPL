#!/usr/bin/env python
from functools import wraps

converters = {}

def register_converter(doc_type):

    def inner_deco(old_func):
        converters[doc_type] = old_func

        @wraps(old_func)
        def new_func(*args, **kwargs):
            print(f"converting {doc_type} with {old_func}")
            return old_func(*args, **kwargs)

        converters[doc_type] = new_func

        return new_func

    return inner_deco


@register_converter('doc')
def spam(old_name, new_name):
    print("In spam!")

@register_converter('pdf')
def ham(old_name, new_name):
    print("In ham!")

print(converters)


# spam('foo.txt', 'foo.doc')
# ham('bar.txt', 'bar.pdf')

files = [
    ('foo.txt', 'doc'),
    ('bar.txt', 'pdf'),
]

for file_name, file_type in files:
    f = converters[file_type]
    converters[file_type](file_name, 'new_file')
