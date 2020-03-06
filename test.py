# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

import requests
import json

AUTH = '''j24kWwQP9x%2BY3SddEsWL3rSb8YqU5O9NsuKA0B6qvHngO7e5Rxj%2BDm49d%2FpGWxWAlPfspOAgsN0urSw00GfSLC1qdOaNuY3QJvBSvBM5hoptevxnQhoACkUpFpLgW3lmBrMAsJEL42Y%3D'''

HEADERS = {
    "authorization": AUTH,
    "content-type": "application/json; charset=UTF-8",
    "Host": "mapi.eyee.com",
    "user-agent": "EYEE/3.4.6 (Xiaomi Xiaomi MI 4LTE; Android 6.0.1)",
}

url = 'https://mapi.eyee.com/capi/exchange/precoupon/coupontrade'
data = {"coupontype": '1', "page": '1', "size": '100', "type": '1'}
headers = HEADERS

# data = json.dumps(data)
resp = requests.post(url=url, data=data, headers=headers)
print(resp.status_code)
print(resp.text)
