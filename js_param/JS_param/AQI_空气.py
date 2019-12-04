import execjs
import requests
import json

# init environment
node = execjs.get()

# params
method = 'GETCITYWEATHER'
city = '重庆'
type = 'HOUR'
start_time = '2018-12-12 07:00:00'
end_time = '2018-12-12 23:00:00'

# compile jacascript
file = 'encryption.js'
ctx = node.compile(open(file, encoding='UTF-8').read())

# get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)

params = ctx.eval(js)

api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})

js_0 = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js_0)
s = json.loads(decrypted_data)
print(s)