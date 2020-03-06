# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(can_run)
        if not can_run:
            print(args)
            print(kwargs)
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func(args):
    return ("Function is running" + args)


can_run = True
print(func('你好'))
# Output: Function is running

can_run = False
print(func('我不好'))
