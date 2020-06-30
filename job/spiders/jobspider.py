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
            #职位名称
            item['Jname'] = post.xpath(
                './header/h1/a/text()').extract()[0].strip()
            #薪水 已废弃 换成了最低薪资和最高薪资
            # item['Jsalary'] = 0
            # #地区
            # item['Jarea'] = ''
            #值位类型
            item['Jtype'] = post.xpath('./div/text()').extract()[0].strip()
            #职位要求
            # item['Jrequirements'] = ''
            # #公司名称
            # item['Jcompany'] = ''
            # #标签
            # item['Jtag'] = ''
            # #福利
            # item['Jwelfare'] = ''
            # #学历要求
            # item['Jeducation'] = ''
            # #经验要求
            # item['Jexperience'] = ''
            # #最低工资
            # item['JminSalary'] = 0
            # #最高工资 均以k为单位，类型为int
            # item['JmaxSalary'] = 0
            # #每年多少薪资数据类型int
            # item['JpayTimes'] = 0
            # #公司类型
            # item['JcomType'] = ''
            # #招聘人数,字符串
            # item['JhireCount']='0'
            yield item
