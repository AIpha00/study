# coding=utf-8
import requests
import json
import re
import csv

s = requests.session()

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"27b34-2ivBrN1isIzhrlVixkDVMEYzatg"',
    'referer': 'https://www.tmall.com/?ali_trackid=2:mm_26632258_3504122_48284354:1582186923_172_1370005755&clk1=33539b37588812d3bec9699d8526140a&upsid=33539b37588812d3bec9699d8526140a',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
}
url = 'https://s.taobao.com/search?q={seed}&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s={page}'
with open('taobao_login_cookies.txt', 'r+', encoding='utf-8') as file:
    cookies_dict = json.load(file)
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
s.cookies = cookies
res_list = []

f = open('taobao_res.csv', 'w+', encoding='utf-8')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
csv_writer.writerow(["商品名", "购买人数", "价格", "店铺名称", "sku"])

for page in range(1, 30):
    wbdata = s.get(url=url.format(seed='nike', page=str((page - 1) * 44) if page >= 2 else page), headers=header)
    if '滑动一下马上回来' in wbdata.text:
        print('出现验证码')
        break
    data_text = re.findall('g_page_config = (.*);', wbdata.text)[0]
    data = json.loads(data_text)
    items = data.get('mods', {}).get('itemlist', {}).get('data', {}).get('auctions', [])
    for item in items:
        price = item.get('view_price', '')
        payment = item.get('view_sales', '')
        name = item.get('raw_title', '')
        nick = item.get('nick', '')
        nid = item.get('nid', '')
        res = {
            'name': name,
            'payment': payment,
            'price': price,
            'nick': nick,
            'nid': nid
        }
        print(res)
        csv_writer.writerow((name, payment, price, nick, str(nid)))
        res_list.append(res)
f.close()
