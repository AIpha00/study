import execjs
import requests
from lxml import etree




USERNAME = 'aiphalv0010@gmail.com'
PASSWORD = 'herococo11'
url = 'http://openlaw.cn/login.jsp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
phantomjs = execjs.get()
session = requests.session()

file = 'encrypt.js'
response = session.get(url=url)
text = response.text
html = etree.HTML(text)
ctx = phantomjs.compile(open(file, encoding='UTF-8').read())
js_pass = "keyEncrypt('{0}')" .format(PASSWORD)
pwd = ctx.eval(js_pass)
print(pwd)
captcha = html.xpath('//img[@id="kaptcha"]/@src')
csrf = html.xpath('//input[@name="_csrf"]/@value')
captcha_url = 'http://openlaw.cn{0}'.format(captcha[0])
captcha_content = session.get(captcha_url).content
with open('./captcha_openlaw.jpg', 'wb') as f:
    f.write(captcha_content)
captcha_input = input('请输入验证码：')
login_post = 'http://openlaw.cn/login'
data = {
    '_csrf': csrf,
    'username': USERNAME,
    'password': pwd,
    'code': captcha_input,
}
login = session.post(url=login_post, data=data, headers=headers)

print(login.status_code)
