'''
@Descripttion: 
@version: 
@Author: Paul
@Date: 2020-06-29 20:42:18
@LastEditors: Paul
@LastEditTime: 2020-06-30 21:19:49
'''
# -*- coding: utf-8 -*-
import json
import re
import random
import scrapy
from urllib import parse
import requests
import execjs


class BossjobSpider(scrapy.Spider):
    name = 'bossJob'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']
    url = ['https://www.zhipin.com/wapi/zpCommon/data/position.json']


'''
@Descripttion:
@version:
@Author: Paul
@Date: 2020-06-29 20:42:18
@LastEditors: Paul
@LastEditTime: 2020-06-30 20:51:22
'''
# -*- coding: utf-8 -*-


class BossjobSpider(scrapy.Spider):
    name = 'bossJob'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']
    url = "https://www.lagou.com/jobs/positionAjax.json"

    def __init__(self, *args, **kwargs):
        self.js = execjs.compile(open("demo\\resource\\lagou.js", "r").read())
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Cookie': '__zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591323218,1593422098,1593474830; __c=1593474830; __g=-; __l=l=%2Fwww.zhipin.com%2Fchongqing%2F&r=&friend_source=0&friend_source=0; t=mG1RNcwCDMtt1o6h; wt=mG1RNcwCDMtt1o6h; _bl_uid=g4kbncav1hs57psCUopt3qF03tII; __zp__pub__=; lastCity=100010000; __zp_stoken__=cc09aAGMeKXk%2FKmM7QDtKAQEXWkwQWR0wWGInTiNwez4vYFdiRx4pehwHI1FybEo8fSA6GFUTcXo1MzpkQW5BQFRDaCAEDw09JG5weQwfXxUzRw9YcD4JGUlVHntVTBxxPxl%2FZwZnBQ0KIT4%3D; __a=16012288.1591323216.1593422098.1593474830.124.3.79.124; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1593494636',
    #     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    # }

    def writeJson(self, data):

        with open('test.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
        print("finished")

    def start_requests(self):
        print("==============requests============")
        cookiesDict = self.run()
        data = {"first": "false", "pn": "", "kd": ""}

        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "referer": "https://www.lagou.com/jobs/list_/p-city_3?px=default",
        }
        yield scrapy.FormRequest(url=self.url, headers=headers, cookies=cookiesDict, formdata=data)

    def run(self):
        print("==============run============")
        main_url = f"http://www.lagou.com/utrack/trackMid.html"
        headers = {
            "user-agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/{random.randint(1, 999)}.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "referer": "https://www.lagou.com/"
        }
        response = requests.get(main_url, headers=headers)
        return self.track_mid_parse(response)

    def track_mid_parse(self, response):
        print("==============track============")
        set_cookie = response.headers["Set-Cookie"]
        user_trace_token_value = re.search(
            "user_trace_token=(.*?);", set_cookie)
        response_time = response.headers["Date"]
        if user_trace_token_value:
            user_trace_token_value = user_trace_token_value.group(1)
            x_http_token = self.js.call(
                "get_token", user_trace_token_value, response_time)
            web_tj = self.js.call("get_webtj_id")
            cookie_dict = {"X_HTTP_TOKEN": x_http_token,
                           "WEBTJ-ID": web_tj,
                           "user_trace_token": user_trace_token_value}
        return cookie_dict

    def parse(self, response):

        result = json.loads(response.text)
        self.writeJson(result)

    def parse(self, response):
        pass
