import asyncio
import aiohttp
import time
import sys

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from ProxyPool.proxypool.db import RedisClient
from ProxyPool.proxypool.setting import *

import logging

# 通过下面的方式进行简单配置输出方式与日志级别
# log_name = 'log/logging.log'
# fh = logging.FileHandler(encoding='utf-8', mode='a+', filename=log_name)
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy:
        :return:
        """
        headers = {
            "Connection": "keep-alive",
            "Host": "www.sogou.com",
            "Pragma": "no-cache",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        }
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试' + proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False,
                                       headers=headers) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用' + proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法 ' + str(response.status) + 'IP' + proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败{}'.format(proxy))

    def run(self):
        """
        测试主函数
        :return:
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余{}个代理'.format(count))
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第{}-{}个代理'.format(start + 1, stop))
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误{}'.format(e.args))
