import json
import re
from .utils import get_page
from pyquery import PyQuery as pq
import logging

# 通过下面的方式进行简单配置输出方式与日志级别
# log_name = 'log/logging.log'
# fh = logging.FileHandler(encoding='utf-8', mode='a+', filename=log_name)
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理：{}'.format(proxy))
            proxies.append(proxy)
        return proxies

    def crawl_test(self):
        return ['127.0.0.1:22222']
