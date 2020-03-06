from collections import Counter
from urllib.parse import urlencode

import redis
import requests

pool = redis.ConnectionPool(host="localhost", port=6379)
conn = redis.Redis(connection_pool=pool)

headers = {
    "Origin": "https://www.nike.com",
    "Referer": "https://www.nike.com/cn/",
    'Sec-Fetch-Mode': 'cors',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "X-NewRelic-ID": "UwcDVlVUGwIHUVZXAQMHUA==",
    "Cookie": "bm_sz=42A1C3ED1E42D0E53B46CE138833E8A0~YAAQ0p7C3eImk75sAQAAn01f8gQERVHcv13L066YKg1+snbS0DYMbDAGOdJbK38goM1yznfQg4fYaoKvRITEo5WHG8iS5XSI68zN+LWg3aJh196EPprF8OdcwyfDBY0q+TG8UleffpT8Z36ibnvJNnRsWr2lspW1R4kdfa2X/8azGOXUhcEfZStuDjmGdQ=="
}


def get_abck(url, headers):
    response = requests.get(url=url)
    cookies = response.headers['Set-Cookie'].split(';')
    res_cookie = []
    set_cookie = []
    for cookie in cookies:
        set_cookie.append(cookie.split(','))
    for sets in set_cookie:
        for set in sets:
            if "_abck" in set:
                print(set)
            if "bm_sz" in set:
                res_cookie.append(set)
            else:
                continue
    headers['Cookie'] = ";".join(res_cookie).replace(" ", "")
    sensor_url = "https://www.nike.com/static/26c6d98637e1818a5b600fe3b42865c"
    sensor_data = input("请手动获取sensor_data:")
    input()
    print(sensor_data)
    sensor_data_dict = {
        "sensor_data": sensor_data
    }
    res_login = requests.post(url=sensor_url, headers=headers, data=sensor_data_dict)
    print(res_login.text)
    cookie_sen = prase_cookie_str(res_login.headers["Set-cookie"])
    print(cookie_sen)
    headers['Cookie'] = headers['Cookie'] + ';' + cookie_sen
    login_url = 'https://unite.nike.com/login?'
    query_data = {
        "appVersion": "630",
        "experienceVersion": "528",
        "uxid": "com.nike.commerce.nikedotcom.web",
        "locale": "zh_CN",
        "backendEnvironment": "identity",
        "browser": "Google Inc.",
        "os": "undefined",
        "mobile": "false",
        "native": "false",
        "visit": "1",
        "visitor": "894b39f0-ce90-4b24-89fb-e9e2b4d08932",
    }
    login_data = {
        'client_id': "HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH",
        'grant_type': "password",
        'password': "Lherococo11",
        'username': "+8613795870040",
        'ux_id': "com.nike.commerce.nikedotcom.web",
    }
    login_url = login_url + urlencode(query_data).replace("+", "%20")
    test_login = requests.options(url=login_url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})
    print(test_login.text, test_login.status_code)
    headers['Host'] = "unite.nike.com"
    resp_login = requests.post(url=login_url, headers=headers, data=login_data)
    if resp_login.status_code == 200:
        print('登录成功')
        print(resp_login.text)
    else:
        print('登录失败', end=' ')
        print(resp_login.text)
        print(resp_login.status_code)


def prase_cookie_str(cookie=None):
    if cookie is None or cookie == '':
        return ''
    result_str = ''
    cookies = cookie.split(';')
    cookie_dict = Counter(cookies)
    for elem in cookie_dict.elements():
        if cookie_dict[elem] == 1:
            _ = elem.split(', ')[-1].strip()
            if '=' in _ and 'path' not in _ and 'Domain' not in _ and 'Path' not in _:
                result_str += _ + ';'
    return result_str


if __name__ == '__main__':
    url = "https://www.nike.com/cn/"
    get_abck(url=url, headers=headers)
