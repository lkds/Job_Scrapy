'''
@Descripttion:
@version:
@Author: Paul
@Date: 2020-06-29 20:42:18
@LastEditors: Paul
@LastEditTime: 2020-07-01 18:21:38
'''
# -*- coding: utf-8 -*-
import json
import logging
import os
import random
import re
import sys
import time
from urllib import parse
from urllib import parse
import execjs
import requests
import scrapy

from job.items import JobItem


# -*- coding: utf-8 -*-
logger = logging.getLogger(__name__)


class lagouJobSpider(scrapy.Spider):
    name = 'lagouJob'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']
    urls = "https://www.lagou.com/jobs/positionAjax.json?city="
    # Post请求的参数
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "referer": "https://www.lagou.com/jobs/list_/p-city_3?px=default",
    }
    # 拉勾中涉及的所有城市
    cities = ["安阳", "安庆", "鞍山", "安顺", "安康", "阿克苏", "阿坝藏族羌族自治州", "阿拉善盟", "北京", "保定", "蚌埠", "包头", "滨州", "宝鸡", "北海", "毕节", "亳州", "巴中", "百色", "本溪", "巴音郭楞", "巴彦淖尔", "白城", "保山", "白银", "博尔塔拉", "白山", "成都", "长沙", "重庆", "长春", "常州", "沧州", "郴州", "常德",
              "赤峰", "潮州", "滁州", "承德", "朝阳", "池州", "楚雄", "昌吉", "崇左", "东莞", "大连", "德州",
              "德阳", "东营", "大庆", "大同", "达州", "大理", "丹东", "德宏", "定西", "迪庆", "鄂州", "恩施",
              "鄂尔多斯", "佛山", "福州", "阜阳", "抚州", "防城港", "抚顺", "阜新", "广州", "贵阳", "桂林", "赣州",
              "广元", "贵港", "广安", "杭州", "合肥", "惠州", "哈尔滨", "海口", "呼和浩特", "邯郸", "菏泽", "湖州", "淮安",
              "衡阳", "海外", "衡水", "黄石", "河源", "黄冈", "怀化", "淮南", "葫芦岛", "汉中", "红河", "淮北", "黄山", "鹤壁",
              "贺州", "海东", "呼伦贝尔", "河池", "鹤岗", "哈密", "和田", "济南", "金华", "嘉兴", "江门", "济宁", "揭阳", "晋中",
              "荆州", "九江", "焦作", "锦州", "吉林", "景德镇", "吉安", "晋城", "荆门", "佳木斯", "酒泉", "济源", "金昌", "鸡西",
              "昆明", "开封", "喀什", "克拉玛依", "廊坊", "兰州", "临沂", "洛阳", "聊城", "连云港", "柳州", "六安", "拉萨", "丽水",
              "吕梁", "龙岩", "临汾", "乐山", "漯河", "泸州", "六盘水", "辽阳", "凉山彝族自治州", "丽江", "莱芜", "辽源", "娄底", "陇南",
              "来宾", "林芝", "绵阳", "马鞍山", "茂名", "梅州", "眉山", "牡丹江", "南京", "宁波", "南昌", "南宁", "南通", "南阳", "南充",
              "内江", "宁德", "南平", "莆田", "濮阳", "平顶山", "盘锦", "萍乡", "攀枝花", "普洱", "平凉", "青岛", "泉州", "清远", "秦皇岛",
              "衢州", "曲靖", "齐齐哈尔", "黔西南", "黔东南", "钦州", "黔南", "庆阳", "七台河", "日照", "深圳", "上海", "苏州", "沈阳", "石家庄",
              "绍兴", "汕头", "宿迁", "商丘", "上饶", "三亚", "宿州", "韶关", "遂宁", "十堰", "邵阳", "三门峡", "随州", "汕尾", "三明", "绥化",
              "三沙", "四平", "商洛", "石嘴山", "朔州", "松原", "石河子", "天津", "太原", "唐山", "台州", "泰安", "泰州", "通辽", "铜仁", "铜陵",
              "铜川", "天水", "台湾", "天门", "铁岭", "通化", "吐鲁番", "武汉", "无锡", "温州", "潍坊", "乌鲁木齐", "芜湖", "威海", "渭南", "梧州",
              "乌海", "乌兰察布", "武威", "吴忠", "文山", "西安", "厦门", "徐州", "咸阳", "新乡", "西宁", "许昌", "襄阳", "邢台", "湘潭", "孝感", "信阳",
              "咸宁", "宣城", "西双版纳", "忻州", "新余", "香港", "湘西土家族苗族自治州", "兴安盟", "锡林郭勒盟", "烟台", "银川", "扬州", "盐城", "宜昌",
              "运城", "岳阳", "宜春", "玉溪", "阳江", "益阳", "榆林", "营口", "宜宾", "玉林", "云浮", "永州", "延边", "延安", "伊犁", "雅安", "鹰潭", "阳泉",
              "郑州", "珠海", "中山", "淄博", "株洲", "肇庆", "遵义", "湛江", "周口", "漳州", "驻马店", "镇江", "张家口", "长治", "枣庄", "资阳", "舟山", "张家界", "张掖", "昭通", "自贡", "中卫"]

    def __init__(self, *args, **kwargs):
        self.js = execjs.compile(open(os.path.join("job","resource","lagou.js"), "r").read())
        self.Jdb = 'lagoujob'
        # self.Jdb = 'jobclean'

    def writeJson(self, data):

        with open('test.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
        print("finished")

    def start_requests(self):
        """
            重写start_requests，调用city url生成函数
        """
        print("==============requests============")
        return self.nextCityURL()

    def run(self):
        """
            对拉勾网发起请求，获取response
        """
        print("==============run============")
        main_url = f"http://www.lagou.com/utrack/trackMid.html"
        headers = {
            "user-agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/{random.randint(1, 999)}.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "referer": "https://www.lagou.com/"
        }
        response = requests.get(main_url, headers=headers)
        return self.track_mid_parse(response)

    def track_mid_parse(self, response):
        """
            根据拉勾网的response构造cookies
            :return dict 生成的cookie字典
        """
        print("==============track============")
        set_cookie = response.headers["Set-Cookie"]
        user_trace_token_value = re.search(
            "user_trace_token=(.*?);", set_cookie)
        response_time = response.headers["Date"]
        if user_trace_token_value:
            user_trace_token_value = user_trace_token_value.group(1)
            x_http_token = self.js.call(
                "get_token", user_trace_token_value, response_time)
            web_tj = self.js.call("get_webtj_id")
            cookie_dict = {"X_HTTP_TOKEN": x_http_token,
                           "WEBTJ-ID": web_tj,
                           "user_trace_token": user_trace_token_value}
        return cookie_dict

    def parse(self, response):
        """
            对response进行处理  reponse格式为Json
        """
        try:
            print("===========parse==========")
            jobInfo = JobItem()
            result = json.loads(response.text)

            jobs = result['content']['positionResult']['result']
            pageNo = result['content']['pageNo']
            city = parse.unquote(response.url.split("?")[-1])
            print("========" + city + "：" + "page :" + str(pageNo) + "======")
            for job in jobs:
            
                jobInfo['Jname'] = job.get('positionName')
                try:
                    
                    salary = self.modifySalary(job.get('salary'))
                    if(salary):
                        jobInfo['JminSalary'] = (int)(salary[0])
                        jobInfo['JmaxSalary'] = (int)(salary[-1])
                except:
                    pass
                paytimes = (int)(job.get('salaryMonth'))
                if (paytimes == 0):
                    paytimes = 12
                jobInfo['JpayTimes'] = paytimes
                jobInfo['Jarea'] = job.get('city')
                jobInfo['Jtype'] = job.get('industryField')
            # jobInfo['Jrequirements'] = job['financeStage']
                jobInfo['Jcompany'] = job.get('companyFullName')
                jobInfo['Jtag'] = "/".join(job.get('industryLables'))
                #
                jobInfo['Jwelfare'] = job.get('positionAdvantage')
                jobInfo['Jeducation'] = job.get('education')
                # todo finished
                jobInfo['Jexperience'] = self.modifyJexperience(
                    job.get('workYear'))

                jobInfo['JcomFinanceStage'] = self.modifycomFinanceStage(job.get(
                    'financeStage'))
                if(job.get('latitude') != None and job.get('longitude') != None):
                    jobInfo['Jlocation'] = "(" + job.get('latitude') + \
                        "," + job.get('longitude') + ")"
                jobInfo['JisSchoolJob'] = job.get('financeStage')
                jobInfo['JcomSize'] = self.modifyComSize(job.get('companySize'))
                jobInfo['JcreatedTime'] = job.get('createTime')
                jobInfo['JisSchoolJob'] = job.get('isSchoolJob')
                # jobInfo['Jsource'] = response.url
                jobInfo['Jsite'] = "拉勾"
                # print(jobInfo)
                yield jobInfo
        except:
            pass
        # 同一城市的翻页
        if (pageNo != 0):
            cookiesDict = self.run()

            data = {"first": "false", "pn": "0", "kd": ""}
            data["pn"] = str(pageNo + 1)
            yield scrapy.FormRequest(url=response.url, headers=self.headers, cookies=cookiesDict, formdata=data)

    def modifyComSize(self, comSize):
        if (comSize.find("少于") != -1 or comSize.find("以上") != -1):
            return re.findall(r'\d+', comSize)[0]
        elif(comSize.find('-') != -1):
            return re.findall(r'\d+\-\d+', comSize)[0]
        else:
            return
    def modifySalary(self, salary):
        return re.findall(r'\d+',salary)

    def modifycomFinanceStage(self, comSize):
        if (comSize.find("轮") != -1):
            if (comSize.find("天使") != -1):
                return "天使轮"
            else:
                return re.findall(r'\w', comSize)[0] + "轮"
        elif (comSize.find("上市") != -1):
            return "上市"
        elif (comSize.find("融资")):
            return "无"

    def modifyJexperience(self, exp):
        if (exp.find("以上") != -1):
            return "10+"
        if (exp.find("以下") != -1):
            return re.findall(r'\d', exp)[0]
        elif (exp.find("-") != -1):
            return re.findall(r'\d+\-\d+', exp)[0]
        else:
            return exp

    def nextCityURL(self):
        """
            构造不同的城市url 并发起post请求
        """
        print("=============next_url===============")

        for city in self.cities:
            #time.sleep(2)
            self.url = "https://www.lagou.com/jobs/positionAjax.json?city={}".format(
                city)
            cookiesDict = self.run()
            # formdata = self.data
            data = {"first": "false", "pn": "0", "kd": ""}
            print("===========" + city + "==========")
            yield scrapy.FormRequest(url=self.url, headers=self.headers, cookies=cookiesDict, formdata=data)

    def saveData(self, jobdict):
        """
          使用items以及pipeline实现爬虫数据持久化
          :params: dict 爬取到的一条信息
        """
        item = JobItem()
        item = jobdict
        yield item
