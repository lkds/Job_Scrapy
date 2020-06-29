# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem

class JobspiderSpider(scrapy.Spider):
    name = 'jobspider'
    allowed_domains = ['paulzzzhang.xyz']
    start_urls = ['http://paulzzzhang.xyz/']

    def parse(self, response):
        item = JobItem()

        for post in response.xpath("//article/div"):
            # print(p)
            item['Jname'] = post.xpath(
                './header/h1/a/text()').extract()[0].strip()
            item['Jtype'] = post.xpath('./div/text()').extract()[0].strip()
            yield item
