# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

import time
import sys

# for i in range(10):
#     print(i, end=" ")
#     # 实时打印信息到控制台
#     sys.stdout.flush()
#
#     time.sleep(0.4)

from functools import lru_cache


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


res = []
for i in range(100000):
    res.append(fib(i))

print(res)

print(len([fib(n) for n in range(100)]))
