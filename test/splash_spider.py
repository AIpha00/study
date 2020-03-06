# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
import requests
from urllib.parse import quote
import json

lua = """
function main(splash)
  splash.image_enabled = false
  assert(splash:go("https://login.taobao.com/member/login.jhtml"))
  change = splash:select(".login-switch")
  change:mouse_click()
  splash:wait(1)
  username = splash:select("#TPL_username_1")
  username:send_text("13795870040")
  password = splash:select("#TPL_password_1")
  password:send_text("herococo11.")
  splash:wait(1)
  login = splash:select("#J_SubmitStatic")
  login:mouse_click()
  splash:wait(1)
  return {
    html = splash:html(),
    png = splash:png(),
    cookies = splash:get_cookies(),
  }
end
"""

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
resp = requests.get(url)
resp_data = json.loads(resp.text)
cookies = ''
for cookie in resp_data.get('cookies', []):
    cookies += '{name}={value}; '.format(name=cookie.get('name', ''), value=cookie.get('value', ''))
print(cookies)
