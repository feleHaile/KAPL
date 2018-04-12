    #!/usr/bin/env python
from functools import wraps, update_wrapper

# function decorators:
#     1. function without params
#         decorator returns replacement
#     2. function with params
#         decorator returns wrapper
#         wrapper returns replacement
#     3. class without params
#         __call__ IS replacement
#     4. class with params
#         __call__ RETURNS replacement

# class decorators:
#     5. function without params
#         __call__ IS replacement
#     6. function with params
#     7. class without params
#     8. class with params

#---------------------------------------------------------------------------------------------------------------
# function without params decorating a function -- the simplest case
#---------------------------------------------------------------------------------------------------------------

# @foo
# def bar():
#     pass
#
# same as
# bar = foo(bar)

def deco_one(wrapped_function):

    @wraps(wrapped_function)
    def _replacement(*args, **kwargs):
        print("GREETINGS from deco_one!")
        result = wrapped_function(*args, **kwargs)
        return result + 1

    return _replacement

#---------------------------------------------------------------------------------------------------------------
# function with params decorating a function
#---------------------------------------------------------------------------------------------------------------

# @foo('blah')
# def bar():
#     pass
#
# same as
# bar  = foo('blah')(bar)
# or,
# wrapper = foo('blah')
# bar = wrapper(bar)


def deco_two(value=None):

    def wrapper(wrapped_function):

        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_two -- value is {0}!".format(value)))
            result = wrapped_function(*args, **kwargs)
            return result + 2

        return _replacement

    return wrapper

#---------------------------------------------------------------------------------------------------------------
# class without params decorating a function
#---------------------------------------------------------------------------------------------------------------

# @foo
# def bar():
#     pass
#
# same as
# bar  = foo(bar)

class deco_three(object):

    def __init__(self, wrapped_function):
        self.__name__ = wrapped_function.__name__
        self._wrapped = wrapped_function

    def __call__(self, *args, **kwargs):
        print("GREETINGS from deco_three!")
        result = self._wrapped(*args, **kwargs)
        return result + 3

#---------------------------------------------------------------------------------------------------------------
# class with params decorating a function
#---------------------------------------------------------------------------------------------------------------

# @foo('blah')
# def bar():
#     pass
#
# same as
# bar  = foo('blah')(bar)
# or,
# wrapper = foo('blah')
# bar = wrapper(bar)

class deco_four(object):

    def __init__(self, value):
        self._value = value

    def __call__(self, wrapped_function):

        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_four -- value is {0}!".format(self._value)))
            result = wrapped_function(*args, **kwargs)
            return result + 4

        return _replacement


@deco_one
@deco_two('APPLE')
@deco_three
@deco_four('BANANA')
def target_function(color, value):
    print(("Hello from target_function -- color is {0} and value is {1}".format(color, value)))
    print(("Target function's name is", target_function.__name__))
    return 10 * value

result = target_function('red', 10)
print(("RESULT is", result))
print(('-' * 50))
result = target_function('green', 45)
print(("RESULT is", result))
print(('-' * 50))
print()
print()


#---------------------------------------------------------------------------------------------------------------
# function without params decorating a class
#---------------------------------------------------------------------------------------------------------------
def deco_five(target_class):
    print("GREETINGS from deco_five!")
    @property
    def _temp(self):
        return self._value1

    target_class.value_one = _temp

    return target_class
#---------------------------------------------------------------------------------------------------------------
# function with params decorating a class
#---------------------------------------------------------------------------------------------------------------
def deco_six(fruit):
    print("GREETINGS from deco_six!")

    def wrapper(target_class):

        target_class._fruit = fruit

        @property
        def _temp(self):
            return self._fruit

        target_class.fruit = _temp

        return target_class

    return wrapper



@deco_five
@deco_six('MANGO')
class target_class(object):

    def __init__(self, v1, v2, v3, v4):
        self._value1 = v1
        self._value2 = v2
        self._value3 = v3
        self._value4 = v4

t1 = target_class('fee', 'fi', 'fo', 'fum')
print(("t1 is", t1))
print(("value_one:", t1.value_one))

print(('-' * 50))
t2 = target_class('eeny', 'meeny', 'miny', 'mo')
print(("t2:", t2))
print(("t2.value_one:", t2.value_one))
print(("t2.fruit:", t2.fruit))

print(('-' * 50))
#---------------------------------------------------------------------------------------------------------------
# class without params decorating a class
#---------------------------------------------------------------------------------------------------------------

class deco_seven(object):
    def __new__(cls, old_class):
        print("GREETINGS from deco_seven!")
        old_class.color = 'blue'
        return old_class

@deco_seven
class target_class(object):
    pass

t1 = target_class()
print((t1.color))
print(("t1 id:", id(t1)))
print((target_class.__name__, t1))

t2 = target_class()
print((t2.color))
print(("t2 id:", id(t2)))

print(('-' * 50))
#---------------------------------------------------------------------------------------------------------------
# class with params decorating a class
#---------------------------------------------------------------------------------------------------------------

class deco_eight(object):
    def __init__(self, color):
        print("GREETINGS from deco_eight!")
        self._color = color

    def __call__(self, old_class):
        old_class.color = self._color
        return old_class

@deco_eight('purple')
class target_class(object):
    pass

t1 = target_class()
print((t1.color))
