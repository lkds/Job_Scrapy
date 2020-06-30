import scrapy
from job.items import JobItem
import sys

class jobSpider(scrapy.Spider):
    # 设置name
    name = "cnzp"
    # 设定域名
    allowed_domains = ["cnzp.cn"]
    # 填写爬取地址
    start_urls = ["https://www.cnzp.cn/job/"]
    def __init__(self):
        self.Jdb = 'cnzp'
    # 编写爬取方法
    def parse(self, response):
        for line in response.xpath('//div[contains(@class,"search_job_list")]'):
            # 初始化item对象保存爬取的信息
            item = JobItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['Jname'] = line.xpath('./div[1]/div[1]/a/text()').extract()[0]
            salary = line.xpath('./div[1]/div[2]/text()').extract()[0]
            if(salary!='面议'):
                salary = salary.split('￥',1)[1]
                item['JmaxSalary'] = round(int(salary.split('-',1)[1])/1000,2)
                item['JminSalary'] = round(int(salary.split('-',1)[0])/1000,2)
            else:
                item['JmaxSalary'] = 0
                item['JminSalary'] = 0
            # item['Jsalary'] = ''
            # item['JpayTimes'] = ''
            # item['Jtype'] = ''
            # item['Jrequirements'] = ''
            # item['Jwelfare'] = ''
            item['Jexperience'] = line.xpath('./div[2]/div[1]/div[1]/span[3]/em/text()').extract()[0]
            item['Jeducation'] = line.xpath('./div[2]/div[1]/div[1]/span[5]/em/text()').extract()[0]
            item['Jarea'] = line.xpath('./div[2]/div[1]/div[1]/span[1]/em/text()').extract()[0]
            item['Jcompany'] = line.xpath('./div[1]/div[3]/a[1]/text()').extract()[0]
            item['Jtag'] = line.xpath('./div[2]/div[2]/div[1]/div/text()').extract()[0]
            if(len(line.xpath('./div[2]/div[2]/div[1]/div/text()').extract())==3):    
                item['JcomSize'] = line.xpath('./div[2]/div[2]/div[1]/div/text()').extract()[2].split('人',1)[0]
                item['JcomType'] = line.xpath('./div[2]/div[2]/div[1]/div/text()').extract()[1]
            else:
                item['JcomSize'] = line.xpath('./div[2]/div[2]/div[1]/div/text()').extract()[1].split('人',1)[0]
                # item['JcomType'] = ''
            if(line.xpath('./div[2]/div[1]/div[2]/@class').extract()[0]=='job_describe_p'):
                if(len(line.xpath('./div[2]/div[1]/div[2]//span/text()').extract())==3):
                    item['JhireCount'] = line.xpath('./div[2]/div[1]/div[2]//span/text()').extract()[0].split('人',1)[0].split('聘',1)[1]
                # else:
                #     item['JhireCount'] = ''
                
            elif(line.xpath('./div[2]/div[1]/div[2]/@class').extract()[0]=='job_welfare_tag'):
                item['Jwelfare'] = ', '.join(line.xpath('./div[2]/div[1]/div[2]//span/text()').extract())

            yield item

        next_url = response.xpath('//div[@class="search_pages"]//a[last()]/@href').extract()
        if next_url:
            yield scrapy.Request(next_url[0],callback=self.parse)