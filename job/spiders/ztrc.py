# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem

class ZtrcSpider(scrapy.Spider):
    name = 'ztrc'
    allowed_domains = ['www.job5156.com']
    start_urls = ['http://www.job5156.com/']

    def parse(self, response):
        # item = JobItem()

        # for post in response.xpath("//article/div"):
        #     # print(p)
        #     item['Jname'] = post.xpath(
        #         './header/h1/a/text()').extract()[0].strip()
        #     item['Jsalary'] = 0
        #     item['Jarea'] = ''
        #     item['Jtype'] = post.xpath('./div/text()').extract()[0].strip()
        #     item['Jrequirements'] = ''
        #     item['Jcompany'] = ''
        #     item['Jtag'] = ''
        #     item['Jwelfare']=''
        #     yield item
        pass