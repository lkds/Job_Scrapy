'''
@Descripttion: 爬取boss直聘city以及industry info
@version:
@Author: Paul
@Date: 2020-06-30 08:10:53
@LastEditors: Paul
@LastEditTime: 2020-06-30 21:27:18
'''
# -*- coding: utf-8 -*-
import scrapy
import json


class JobinfoSpider(scrapy.Spider):
    name = 'JobInfo'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/jobs/allCity.html']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591323218,1593422098,1593474830; __c=1593474830; __g=-; __l=l=%2Fwww.zhipin.com%2Fchongqing%2F&r=&friend_source=0&friend_source=0; t=mG1RNcwCDMtt1o6h; wt=mG1RNcwCDMtt1o6h; _bl_uid=g4kbncav1hs57psCUopt3qF03tII; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1593476345; __zp_stoken__=cc09aABcQaXUsKTM7ICIsHDIQSmNmDG9pLGVsSH0Hc2ggASdkR3gRYSxvZTEyB2wsfSA6GFUTbwcUbzBkRA1hXx0sK1czGDJdKWh7FgwfXxUzRx9%2BG35pXyFlBUMzTBxxPxl%2FZwZnBQ0KIT4%3D; __a=16012288.1591323216.1593422098.1593474830.67.3.22.67',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    def writeJson(self, data):

        print(data)
        with open('industry.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
        print("finished")

    def parse(self, response):
        for items in response.xpath('//*[@id="main_container"]/div/div[1]/table[2]/tbody/tr[1]/td[2]/ul/li[1]/a'):
            print(items)
