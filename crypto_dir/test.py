'''
 author: lvsongke@oneniceapp.com
 data:2019/09/02
'''
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
headers['Cookie'] = 'SESSIONID=e9e3eabd-c5c8-4822-a7e4-444deaa59e57;XSRF-TOKEN=aba1f9ef-66ad-4ffe-b632-17a7ce5e51f5'
url_order = 'https://www.adidas.com.cn/orderHistory?orderType=0'
resp = requests.get(url_order, headers=headers, verify=False)
print(resp.text)
