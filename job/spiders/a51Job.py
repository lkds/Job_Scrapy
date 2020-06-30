# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem
from scrapy.http import Request
import re
from urllib import parse

class A51jobSpider(scrapy.Spider):
    name = '51Job'
    allowed_domains = ['51job.com']
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,"
    offset = 1
    start_urls = [url + str(offset) + ".html?"]

    # 处理请求的方法
    def parse(self, response):
        # yield item
        links = response.xpath('//div[@class="el"]/p/span/a/@href').extract()
        # 迭代取出每个集合里的链接
        for link in links:
            # 提取列表里每个链接，发送请求并调用callback处理
            yield scrapy.Request(link, callback=self.parse_item)
        if self.offset <= 2:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset) + ".html?", callback=self.parse)

    # 处理详情页信息的方法
    def parse_item(self, response):
        item = JobItem()
        textlist = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').extract()
        # print(textlist)
        textlen = str(textlist).replace('\xa0', '').split('[')[1].split(']')[0].split('|')
        if len(textlen) > 4 :
            # 公司名字
            # item['Jcompany'] = response.xpath('//div[@class="in"]/div/p/a/@title').extract()[0]
            item['Jcompany'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/@title').extract()[0]
            # 职位名字
            item['Jname'] = response.xpath('//div[@class="in"]/div[@class="cn"]/h1/@title').extract()[0]
            # 工作地点
            Jarea = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[0]
            # item['Jarea'] = Jarea.strip().split("-")[0]
            item['Jarea'] = Jarea.strip()
            # 公司福利
            Jwelfare = response.xpath('//div[@class="jtag"]/div/span/text()').extract()
            if Jwelfare:
                item['Jwelfare'] = ",".join(Jwelfare)
            # 薪水
            Jsalary = response.xpath('//div[@class="in"]/div/strong/text()').extract()
            # if Jsalary == []:
            #     item['Jsalary'] = ""
            # else:
            #     item['Jsalary'] = Jsalary
            if Jsalary != []:
                if '-' in Jsalary[0]:
                    JminSalary = Jsalary[0].split("-")[0]
                    JmaxSalary = Jsalary[0].split("-")[1].replace('\n', '')
                    JmaxSalary2 = re.split('万|千', JmaxSalary)[0]
                    item['JminSalary'] = JminSalary
                    item['JmaxSalary'] = JmaxSalary2
            # 学历
            Jeducation = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[2]
            item['Jeducation'] = Jeducation.strip()
            # 工作经验
            Jexperience = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[1]
            item['Jexperience'] = Jexperience.strip().replace("经验", "").replace("无工作", "不限")
            # 招的人数
            JhireCount = response.xpath('//div[@class="cn"]/p[2]/text()').extract()[3]
            item['JhireCount'] = JhireCount.strip()
            # 要求
            list = response.xpath(
                '//div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/ol/li/text() | //div[@class="tCompany_main"] \
                //div[@class="bmsg job_msg inbox"]/p/span/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"] \
                /p/b/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/text() | //div[@class="tCompany_main"] \
                //div[@class="bmsg job_msg inbox"]/div/text() | //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/text() | \
                //div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/ol/li/p/span/text()').extract()
            item['Jrequirements'] = "".join(list).strip().replace("岗位职责:", "").replace("职位描述:", "").replace(" ", "")
            # 公司类型
            item['JcomType'] = response.xpath('//div[@class="com_tag"]/p[1]/text()').extract()[0]
            # item['Jtag']=''
            item['Jtype']=response.xpath('//div/p[@class = "fp"]/a[@class = "el tdn"]/text()').extract()[0]
            # 交给管道文件处理数据
            # print("x")
            # print(item)
            yield item