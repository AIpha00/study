from ProxyPool.proxypool.tester import Tester
from ProxyPool.proxypool.db import RedisClient
from ProxyPool.proxypool.crawler import Crawler
from ProxyPool.proxypool.setting import *
import sys

import logging

# 通过下面的方式进行简单配置输出方式与日志级别
# log_name = 'log/logging.log'
# fh = logging.FileHandler(encoding='utf-8', mode='a+', filename=log_name)
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)
