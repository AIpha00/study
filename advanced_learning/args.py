# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from functools import reduce


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    print(argv)
    for arg in argv:
        print("another arg through *argv:", arg)


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print('{key} == {value}'.format(key=key, value=value))


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))

number_list = range(-5, 5)
less_than_zero = filter(lambda x: x >= 0, number_list)
print(list(less_than_zero))

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print('*' * 100)
print(product)

test_var_args('yasoob', 'python', 'eggs', 'test', 'java')
greet_me(name='python', age='15')
args = ('two', 3, 5)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(*args)
test_args_kwargs(**kwargs)
