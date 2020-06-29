# -*- coding: utf-8 -*-
import scrapy


class BossjobSpider(scrapy.Spider):
    name = 'bossJob'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        pass
