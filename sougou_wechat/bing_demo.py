import time
import asyncio

from random import randint
from urllib.parse import urlencode, quote

import backoff
import aiohttp

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36',
}


async def https_bing(keyword: str = 'site:baidu.com'):
    params = {
        'q': keyword,
    }
    url = f"https://cn.bing.com/search?{urlencode(params, doseq=True)}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.text()


if __name__ == '__main__':
    html = asyncio.run(https_bing())
