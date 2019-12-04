# coding: utf8
# AIpha


import requests
import time
from urllib.parse import urlencode, quote
import uuid
from lxml import etree
import random
import re

seed = "海贼王"
query_url = "https://weixin.sogou.com/weixin?type=2&query={}".format(quote(seed))
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "weixin.sogou.com",
    "Pragma": "no-cache",
    "Referer": query_url,
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}


def get_cookie(url):
    response = requests.get(url, headers=headers, verify=False)
    cookies = response.headers['Set-Cookie'].split(';')
    res_cookie = []
    set_cookie = []
    for cookie in cookies:
        set_cookie.append(cookie.split(','))
    for sets in set_cookie:
        for set in sets:
            if 'SNUID' in set or 'SUID' in set:
                res_cookie.append(set)
            else:
                continue
    print(res_cookie)
    headers['Cookie'] = ';'.join(res_cookie)
    html = etree.HTML(response.text)
    # link_list = html.xpath('//a[@uigs="account_article_0"]/@href')
    link_list = html.xpath('//ul[@class="news-list"]//a/@href')
    get_suv(res_cookie[0])
    headers_xq = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "mp.weixin.qq.com",
        "Pragma": "no-cache",
        "Referer": query_url,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    for link in link_list:
        # print(link)
        b = int(random.random() * 100) + 1
        a = link.find("url=")
        c = link.find("&k=")
        result_link = (link + "&k=" + str(b) + "&h=" + link[a + 4 + 21 + b: a + 4 + 21 + b + 1])
        print(result_link)
        resp = requests.get(url="https://weixin.sogou.com" + result_link, headers=headers, verify=False)
        rel_url = re.findall("\'(\S+?)\';", resp.text, re.S)
        rel_url = ''.join(rel_url)
        xq_resp = requests.get(url=rel_url, headers=headers_xq, verify=False)
        html = etree.HTML(xq_resp.text)
        title = html.xpath("normalize-space(.//h2[@class='rich_media_title']//text())")
        print('put successful:{}'.format(title))


def get_suv(snuid):
    data = {
        "uigs_cl": "first_click",
        "uigs_refer": "",
        "uigs_t": str(int(round(time.time() * 1000))),
        "uigs_productid": "vs_web",
        "terminal": "web",
        "vstype": "weixin",
        "pagetype": "result",
        "channel": "result_account",
        "s_from": "",
        "sourceid": "",
        "type": "weixin_search_pc",
        "uigs_cookie": "SUID%2Csct",
        "uuid": uuid.uuid1(),
        "query": seed,
        "weixintype": "1",
        "exp_status": "-1",
        "exp_id_list": "0_0",
        "wuid": "",
        "snuid": snuid.split("=")[-1],
        "rn": "1",
        "login": "0",
        "uphint": "0",
        "bottomhint": "0",
        "page": "1",
        "exp_id": "null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9",
        "time": "20429",
    }
    suv_url = "https://pb.sogou.com/pv.gif?" + urlencode(data)

    response = requests.get(suv_url, verify=False)
    print(response)
    cookies = response.headers['Set-Cookie'].split(';')
    res_cookie = []
    set_cookie = []
    for cookie in cookies:
        set_cookie.append(cookie.split(','))
    for sets in set_cookie:
        for set in sets:
            if 'SUV' in set:
                res_cookie.append(set)
            else:
                continue
    print(res_cookie)
    headers['Cookie'] = (headers['Cookie'] + ';' + res_cookie[0]).strip()
    return res_cookie[-1]


def param():
    '''TODO:详情页解析'''
    pass


def get_xq_url(response):
    '''TODO：获取详情页URL'''
    pass


def get_rel_url():
    '''            (function() {
                $("a").on("mousedown click contextmenu", function() {
                    var b = Math.floor(100 * Math.random()) + 1
                      , a = this.href.indexOf("url=")
                      , c = this.href.indexOf("&k=");
                    -1 !== a && -1 === c && (a = this.href.substr(a + 4 + parseInt("26") + b, 1),
                    this.href += "&k=" + b + "&h=" + a)
                })
            }'''
    pass


if __name__ == '__main__':
    snuid = get_cookie(query_url)
