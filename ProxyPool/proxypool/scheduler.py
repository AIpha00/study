import time
from multiprocessing import Process
from ProxyPool.proxypool.api import app
from ProxyPool.proxypool.getter import Getter
from ProxyPool.proxypool.tester import Tester
from ProxyPool.proxypool.db import RedisClient
from ProxyPool.proxypool.setting import *
import asyncio

import logging


# # 通过下面的方式进行简单配置输出方式与日志级别
# log_name = 'log/logging.log'
# fh = logging.FileHandler(encoding='utf-8', mode='a+', filename=log_name)
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            logging.info('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        # if RedisClient().db.exists(REDIS_KEY):
        #     print('清空之前剩余代理')
        #     RedisClient().db.delete(REDIS_KEY)
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
