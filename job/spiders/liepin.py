# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem

class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?compkind=&dqs=', '&pubTime=&pageSize=40&salary=&compTag=&sortFlag=&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=', '&compscale=&key=&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E1p1Hf6Iytm4nd3ac31P45g&d_sfrom=search_fp&d_ckId=265c31fdf5b58dbf7dbf4ccb9f6ef9fb&d_curPage=0&d_pageSize=40&d_headId=430993f27c1c7d527f9c04ec57996860&curPage=']
    
    
    def __init__(self):
        self.Jdb = 'liepin'



    def start_requests(self):

        # 城市：北京 上海 广州 深圳 天津 苏州 重庆 南京 杭州 大连 成都 武汉
        Cities = ['010', '020', '050020', '050090', '030', '060080', '040', '060020', '070020', '210040', '280020', '170020']

    # 行业： 电子商务 游戏产业 计算机软件 IT服务 电子/芯片/半导体 通信业 计算机/网络设备 房地产/建筑 规划/设计/装潢 房地产服务 银行 保险 基金/证券/投资 会计/审计 信托/担保/拍卖
        Industries =['040', '420','010','030', '050', '060', '020', '080', '100', '090', '080', '130','140','150','430','500']
        
        for city in Cities:
            for industry in Industries:
                for i in range(0,20):
                    print("here")
                    print(self.start_urls[0])
                    yield scrapy.Request(url = self.start_urls[0]+city+self.start_urls[1]+industry+self.start_urls[2]+str(i))


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


            # item['Jsalary'] = post.xpath("//span[@class='text-warning']/text()").extract()[0].encode("utf-8")
            item['Jarea'] = post.xpath("./div/div[1]/p[1]/*[@class='area']/text()").extract()[0].split('-')[0]

            JcomFinanceStage0 = post.xpath("./div/div[2]/p[2][@class='field-financing']/span/text()").extract()[0].strip()
            if '未上市' in JcomFinanceStage0 or '未融资' in JcomFinanceStage0:
                item['JcomFinanceStage'] = '无'
            elif '上市' in JcomFinanceStage0:
                item['JcomFinanceStage'] = '上市'
            elif '轮' in JcomFinanceStage0:
                item['JcomFinanceStage'] = JcomFinanceStage0.split('及')[0]
            elif '战略融资' in JcomFinanceStage0:
                item['JcomFinanceStage'] = '战略融资'
            else :
                item['JcomFinanceStage'] = ''

            # item['JcomFinanceStage'] = post.xpath("./div/div[2]/p[2][@class='field-financing']/span/text()").extract()[0].strip()
            
            item['JcomType'] = post.xpath("//div[@class='selected-condition']/dl/dd/span[2]/a/text()").extract()[0].replace('×','').strip()
            # //*[@id="sojob"]/div[1]/form/div[2]/div/div[2]/dl/dd/span[2]/a

            # post.xpath('./div[1]/p[1]/span[2]/text()').extract()[0].encode("utf-8")
            item['Jcompany'] = post.xpath("./div/div[2]/p[1][@class='company-name']/a/text()").extract()[0].strip()

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
            Jeducation0 = post.xpath("./div/div[1]/p[1]/span[@class='edu']/text()").extract()[0]
            if '不限' in Jeducation0:
                item['Jeducation'] = '不限'
            elif '本科' in Jeducation0:
                item['Jeducation'] = '本科'
            elif '及' in Jeducation0:
                item['Jeducation'] = Jeducation0.split('及')[0]


            # item['Jeducation'] = post.xpath("./div/div[1]/p[1]/span[@class='edu']/text()").extract()[0]



            Jexperience0 = post.xpath("./div/div[1]/p[1]/span[3]/text()").extract()[0]
            if '年' in Jexperience0 :
                item['Jexperience'] = Jexperience0.replace('年', '')
            elif '不限' in Jexperience0 :
                item['Jexperience'] = '不限'

            # item['Jexperience'] = post.xpath("./div/div[1]/p[1]/span[3]/text()").extract()[0]
            item['JcreatedTime'] = post.xpath("./div/div[1]/p[@class='time-info clearfix']/time/@title").extract()[0].replace('年','-').replace('月','-').replace('日','')
            item['Jsource'] = response.url
            item['Jsite'] = '猎聘网'

            print(item)
            yield item

        
       