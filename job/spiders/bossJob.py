'''
@Descripttion: 
@version: 
@Author: Paul
@Date: 2020-06-29 20:42:18
@LastEditors: Paul
@LastEditTime: 2020-06-30 08:24:27
'''
# -*- coding: utf-8 -*-
import scrapy


class BossjobSpider(scrapy.Spider):
    name = 'bossJob'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']
    url = ['https://www.zhipin.com/wapi/zpCommon/data/position.json']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'lastCity=101040100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591323218,1593422098,1593474830; __c=1593474830; __g=-; __l=l=%2Fwww.zhipin.com%2Fchongqing%2F&r=&friend_source=0&friend_source=0; t=mG1RNcwCDMtt1o6h; wt=mG1RNcwCDMtt1o6h; _bl_uid=g4kbncav1hs57psCUopt3qF03tII; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1593476345; __zp_stoken__=cc09aABcQaXUsKTM7ICIsHDIQSmNmDG9pLGVsSH0Hc2ggASdkR3gRYSxvZTEyB2wsfSA6GFUTbwcUbzBkRA1hXx0sK1czGDJdKWh7FgwfXxUzRx9%2BG35pXyFlBUMzTBxxPxl%2FZwZnBQ0KIT4%3D; __a=16012288.1591323216.1593422098.1593474830.67.3.22.67',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    def parse(self, response):
        pass
