# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem

class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=&sortFlag=&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=040&compscale=&key=&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E1p1Hf6Iytm4nd3ac31P45g&d_sfrom=search_fp&d_ckId=265c31fdf5b58dbf7dbf4ccb9f6ef9fb&d_curPage=0&d_pageSize=40&d_headId=430993f27c1c7d527f9c04ec57996860&curPage=']
    offset = 0

    def start_requests(self):
        for i in range(0,50):
            yield scrapy.Request(url = self.start_urls[0]+str(i))


    def parse(self, response):
        item = JobItem()
        # print("here")
        # print(response.xpath('//*[@id="sojob"]/div[2]').extract())
        # for post in response.xpath('//*[@id="sojob"]/div[2]/div/div[1]/div[1]/ul/li'):
        for post in response.xpath("//ul[@class='sojob-list']/li"):
            # print(item.extract())
 
            item['Jname'] = post.xpath('./div/div[1]/h3/a/text()').extract()[0].strip()
            if  '-' in post.xpath("./div/div[1]/p[1]/span[@class='text-warning']/text()").extract()[0]:   
                item['JminSalary'] = int(post.xpath("./div/div[1]/p[1]/span[@class='text-warning']/text()").extract()[0].split('·')[0].split('-')[0])

                item['JmaxSalary'] = int(post.xpath("./div/div[1]/p[1]/span[@class='text-warning']/text()").extract()[0].split('·')[0].split('-')[1].split('k')[0])
                
                item['JpayTimes'] = int(post.xpath("./div/div[1]/p[1]/span[@class='text-warning']/text()").extract()[0].split('·')[1].split('薪')[0]) 
            else:
                item['JminSalary'] = int(0)

                item['JmaxSalary'] = int(0)
                
                item['JpayTimes'] = int(0)

            # item['Jsalary'] = post.xpath("//span[@class='text-warning']/text()").extract()[0].encode("utf-8")
            item['Jarea'] = post.xpath("./div/div[1]/p[1]/*[@class='area']/text()").extract()[0]
            
            item['Jtype'] = ""
            item['JcomType'] = post.xpath("./div/div[2]/p[2][@class='field-financing']/span/text()").extract()[0].strip()
            item['Jrequirements'] = ""
            # post.xpath('./div[1]/p[1]/span[2]/text()').extract()[0].encode("utf-8")
            item['Jcompany'] = post.xpath("./div/div[2]/p[1][@class='company-name']/a/text()").extract()[0].strip()
            item['Jtag'] = ""

            # welfares = []
            
            # 为了计算当中span的次数
            # string1 = post.xpath("./div/div[2]/p[3][@class='temptation clearfix']").extract()[0] 
            # string2 = 'span'
            # times = int(string1.count(string2) / 2)
            spanFather = post.xpath('./div/div[2]/p[@class="temptation clearfix"]/span')
            item['Jwelfare'] = ','.join([span.xpath('./text()').extract()[0] for span in spanFather])
                
            

            # for i in range(1,times+1):
            #     string1 = "./div/div[2]/p[3][@class='temptation clearfix']/span["+str(i)+"]/text()"
            #     welfares.append(post.xpath(string1).extract()[0])
            # item['Jwelfare'] = ','.join(welfares)
        
            item['Jeducation'] = post.xpath("./div/div[1]/p[1]/span[@class='edu']/text()").extract()[0]
            item['Jexperience'] = post.xpath("./div/div[1]/p[1]/span[3]/text()").extract()[0]
            print(item)
       
        yield item

        
       