# -*- coding: utf-8 -*-
import scrapy
import time
import json
from job.items import JobItem
import urllib.parse
import http.cookiejar
import urllib.request
import re


class DajiejobSpider(scrapy.Spider):
    name = 'dajie'
    allowed_domains = ['so.dajie.com']
    start_urls = ['https://so.dajie.com/']
    curPage = 1
    cookie = ""
    url = 'https://so.dajie.com/job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=1&positionFunction=&_CSRFToken=Zm7ka3A7nTyN_9zo9OzQpCZE9S4RnD06U4r5CQ**&ajax=1'
    # 加上请求头，伪装成浏览器访问
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        #"content-type": "text/html;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400",
        "referer": "https://so.dajie.com/job/search"
    }
    formData = {}

    def start_requests(self):
        # 使用CookieJar获得cookie值
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        session = opener.open("https://so.dajie.com/job/search")
        session_cookie = re.findall(r"SO_COOKIE_V2=.+?;", str(session.info()))[0].split("=")[1]
        self.cookie = session_cookie.strip(";")
        return [self.next_request()]
    # 处理请求的方法
    def parse(self, response):
        print("request -> " + response.url)
        try:
            # 取响应信息中的响应体并进行解码
            html = json.loads(response.body.decode("utf-8"))
        except ValueError:
            print(response.body)
            yield self.next_request()
        # 判断获取信息是否成功
        if (html.get("result") == 0):
            # 打印招聘信息的数量
            print("Job Num:" + str(html.get('data').get('total')))
            results = html.get('data').get('list')
            if len(results) > 0:
                for result in results:
                    item = JobItem()
                    Salary = []
                    Salary = result.get('salary').strip().replace(" ", "").replace("/月", "").replace("K", "").split("-")
                    # 最低工资
                    item['JminSalary'] = Salary[0]
                    # 最高工资
                    item['JmaxSalary'] = Salary[1]
                    # 年薪
                    item['JpayTimes'] = ''#float( item['JminSalary'] + item['JmaxSalary'] ) / 2
                    # 工作地点  
                    item['Jarea'] = result.get('pubCity')
                    # 职位类型
                    item['Jtype'] = result.get('industryName')
                    # 公司规模
                    #item['company_size'] = result.get('scaleName')
                    # 职位名字
                    item['Jname'] = result.get('jobName')
                    # 经验要求
                    item['Jexperience'] = result.get('pubEx')
                    # 学历要求
                    item['Jeducation'] = result.get('pubEdu')
                    # 公司名字
                    item['Jcompany'] = result.get('compName')
                    # 职位标签
                    item['Jtag'] = ''
                    # 公司福利
                    item['Jwelfare'] = ''
                    # 职位要求
                    item['Jrequirements'] = ''
                    # 招聘人数
                    item['JhireCount']=''
                    yield item
            # 取得网页总页数
            totalPage = html.get('data').get("totalPage")
            self.curPage = self.curPage + 1
            if (self.curPage <= totalPage):
                self.url = 'https://so.dajie.com/job/ajax/search/filter?keyword=&order=0&city=&recruitType=&salary=&experience=&page=' + str(
                    self.curPage) + '&positionFunction=&_CSRFToken=&ajax=1'
                yield self.next_request()
        else:
            #如果信息获取失败，十秒后再次获取
            time.sleep(10)
            yield self.next_request()

    def next_request(self):
        print("dajie page:" + str(self.curPage))
        return scrapy.http.FormRequest(url=self.url, cookies={"SO_COOKIE_V2": self.cookie},
                                       formdata=self.formData, headers=self.headers, method="GET")
