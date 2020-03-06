# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

import time
from random import randint, sample
import hashlib
import requests


def hex5(value):
    _hex5 = hashlib.md5()
    _hex5.update(value.encode('utf-8'))
    return _hex5.hexdigest()


action = "".join([str(randint(1,9)) for _ in range(5)])

tim = round(time.time())

randstr = "".join(sample([chr(_) for _ in range(65, 91)], 5))

value = hex5(action+str(tim)+randstr)

url = 'http://127.0.0.1:8848/capt?action={}&tim={}&randstr={}&sign={}'.format(action, tim, randstr, value)
print(url)
resp = requests.get(url)

print(resp.text)
