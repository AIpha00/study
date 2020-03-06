# -*- coding: utf-8 -*-
import logging

from pymongo import MongoClient


class MongoCli(object):
    connect = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017
        self.user = 'root'
        self.password = ''
        self.db = ''

    def get_connect(self):
        """
        返回连接
        :return:
        """
        if self.connect:
            return self.connect
        try:
            self.connect = MongoClient(host=self.host, port=self.port)
            if self.user and self.password:
                self.connect[self.db].authenticate(self.user, self.password)
            return self.connect
        except Exception as e:
            logger.error(e)
        return False
