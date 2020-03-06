# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""


# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/20
"""

from scrapy import Request
from scrapy.utils.project import get_project_settings
from urllib.parse import urlencode

from snkrs_bot.items.doc_Item import DocItem
from snkrs_bot.spiders.base import BaseDaemon


class PaquSpider(BaseDaemon):
    name = 'paqu_spider'

    settings = get_project_settings()
    log_file = settings.get('LOG_FILE', '')
    custom_settings = {
        'LOG_FILE': log_file.replace('scrapy.log', '{name}.log'.format(name=name)),
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

    sku_url = 'https://service.paquapp.com/api/v2/toybox/brands/'
    pic_base_url = "http://res.paquapp.com/"
    search_url = 'https://service.paquapp.com/api/v1/user/search/users/?'

    def test_paqu(self):
        """
        葩趣,测试入口
        """
        self.onetime = True
        users = [{
            '_id': 13795870040,
        },
        ]
        for user in users:
            yield self.request_paqu(user)

    def arg_paqu_spider(self):
        """
        葩趣爬虫正式入口
        """
        self.onetime = True
        user = self.utils.str2json(self.extra)
        print(user)
        yield self.request_search(user)

    def request_search(self, user):
        word = user.get('key', '')
        query_data = {
            'word': word,
            'count': '20',
            'page': '1',
            'system_version': '6.0.1',
            'platform': 'Android',
            'version': '4.0.1',
            'device_model': 'MuMu',
            'screen_width': '640',
            'device_identify': '90d30b5f5d9f6772',
            'screen_height': '1024',
            'net_status': '1'
        }
        url = self.search_url + urlencode(query_data)
        return Request(url=url,
                       callback=self.parse_paqu,
                       meta={
                           'user': user,
                       },
                       dont_filter=True
                       )

    def request_paqu(self, user=None):
        return Request(self.sku_url,
                       callback=self.parse_paqu,
                       meta={
                           'user': user,
                       },
                       dont_filter=True,
                       )

    def parse_paqu(self, response):
        user = response.meta.get('user', {})
        data = self.utils.str2json(response.text)
        for userinfo in data['data']:
            userinfo = userinfo['user']
            if user['key'] != userinfo['nickname']:
                continue
            item = {}
            item['type'] = '4'
            item['id'] = userinfo['id']
            # userinfo['avatar'] = self.pic_base_url + userinfo['avatar']
            # desc = userinfo['desc']
            # if userinfo['desc'] is None:
            #     desc = ""
            # item['raw_desc'] = desc
            # item['raw_pic'] = userinfo['avatar']
            # item['raw_url'] = ''
            # item['raw_data'] = userinfo
            # save = DocItem(kafka=True, topic='spider-user-result')
            # save.push(item)
            # yield save