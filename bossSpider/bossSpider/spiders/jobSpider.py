# -*- coding: utf-8 -*-
import scrapy


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['https://www.zhipin.com/']
    start_urls = ['http://https://www.zhipin.com//']

    def parse(self, response):
        pass
