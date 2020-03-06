import tornado.ioloop
import tornado.web
import hashlib
import os
import json
from datetime import datetime
from time import time
from notone_crypto import CryptoNotOne
from common.mongo_client import MongoCli


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class RSAMainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("rsa.html")


class MouseMoveHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("mousemove.html")


class RSAHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        params = self.request.arguments  # 获取请求正文
        encrypt = params.get('encrypt')[0].decode('utf-8')
        password = params.get('password')[0].decode('utf-8')
        username = params.get('username')[0].decode('utf-8')
        mon_cli = MongoCli().get_connect()
        db = mon_cli['taobao_crypto']
        db['pw_encrypt'].insert_one({'username': username, 'password': password, 'encrypt': encrypt})
        self.write({'code': True, 'msg': '入库成功'})


class FetHandler(tornado.web.RequestHandler):
    content = '''
    <br/>驾一叶之扁舟，举匏樽以相属。寄蜉蝣于天地，渺沧海之一粟。哀吾生之须臾，羡长江之无穷。挟飞仙以遨游，抱明月而长终。知不可乎骤得，托遗响于悲风。
    '''
    _crypto = CryptoNotOne()

    ticket = _crypto.get_key(16)

    @staticmethod
    def deltes(tp):
        # 将前端传递的时间戳与当前时间戳对比并返回差值秒数
        tamp = int(tp)
        now = round(time())
        delta = datetime.fromtimestamp(now) - datetime.fromtimestamp(tamp)
        return delta.total_seconds()

    @staticmethod
    def hex5(value):
        manipulator = hashlib.md5()
        manipulator.update(value.encode('utf-8'))
        return manipulator.hexdigest()

    def comparison(self, actions, tim, randstr, sign):
        value = actions + tim + randstr + self.ticket
        hexs = self.hex5(value)
        if sign == hexs:
            return True
        return False

    def crypto_check(self, text):
        encrypt_en = self._crypto.encrypt(self.ticket, 'nishizhu')
        if text == encrypt_en:
            return True
        return False

    def get(self, *args, **kwargs):
        params = self.request.arguments  # 获取请求正文
        actions = params.get('action')[0].decode('utf-8')
        tim = params.get('tim')[0].decode('utf-8')
        randstr = params.get('randstr')[0].decode('utf-8')
        sign = params.get('sign')[0].decode('utf-8')
        captcha = params.get('captcha')[0].decode('utf-8')
        ticket = params.get('validata', '')[0].decode('utf-8')
        seconds = self.deltes(tim)
        if self.comparison(actions, tim, randstr, sign) and seconds < 3 and ticket == self.ticket and self.crypto_check(
                captcha):
            self.write(self.content)
        else:
            self.set_status(403)


class CaptHandler(FetHandler):
    ticket = ''

    def get(self, *args, **kwargs):
        params = self.request.arguments  # 获取请求正文
        actions = params.get('action')[0].decode('utf-8')
        tim = params.get('tim')[0].decode('utf-8')
        randstr = params.get('randstr')[0].decode('utf-8')
        sign = params.get('sign')[0].decode('utf-8')
        seconds = self.deltes(tim)
        result = {
            'status': True,
            'validata': ''
        }
        if self.comparison(actions, tim, randstr, sign) and seconds < 1.5:
            validata = super(CaptHandler, self).ticket
            result['validata'] = validata
            self.write(json.dumps(result))
        else:
            result['status'] = False
            self.write(json.dumps(result))


def make_app():
    return tornado.web.Application(
        [(r'/', MainHandler), (r'/fet', FetHandler), (r'/capt', CaptHandler), (r'/rsa', RSAMainHandler),
         (r'/rsa/insert', RSAHandler), (r'/mousemove', MouseMoveHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8206)
    tornado.ioloop.IOLoop.current().start()
