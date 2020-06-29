# -*- coding: utf-8 -*-
import scrapy


class DajiespiderSpider(scrapy.Spider):
    name = 'dajieSpider'
    allowed_domains = ['job.dajie.com']
    start_urls = ['http://job.dajie.com/']

    def parse(self, response):
       #item = JobItem()

        for post in response.xpath('//*[@id="container_jobList"]/ul/li[1]'):
         
            Jname = post.xpath('./div[2]/p[1]/a[1]//*[@id="container_jobList"]/ul/li[1]/div[2]/p[1]/a[1]').extract()
            print(Jname)
            # item['Jsalary'] = post.xpath('./div[2]/p[2]/span[1]').extract()
            # item['Jarea'] = post.xpath('./div[2]/p[2]/span[2]').extract()
            # item['Jtype'] = post.xpath('./div[3]/p[2]/span[1]').extract()
            # item['Jrequirements'] = post.xpath('./div[2]/p[2]/span[2]').extract(
            # item['Jcompany'] = ''
            # item['Jtag'] = ''
            # item['Jwelfare']=''
        #     yield item
        # return item
        # print item['Jname']
        
    pass
