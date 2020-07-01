
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Jname = scrapy.Field()
    JminSalary = scrapy.Field()
    JmaxSalary = scrapy.Field()
    JpayTimes = scrapy.Field()
    Jarea = scrapy.Field()
    Jtype = scrapy.Field()
    Jrequirements = scrapy.Field()
    Jcompany = scrapy.Field()
    Jtag = scrapy.Field()
    Jwelfare = scrapy.Field()
    # 学历
    Jeducation = scrapy.Field()
    # 工作经验
    Jexperience = scrapy.Field()
    # 公司类型
    JcomType = scrapy.Field()
    # 招聘人数
    JhireCount = scrapy.Field()
    # 公司规模
    JcomSize = scrapy.Field()
    # 发布时间
    JcreatedTime = scrapy.Field()
    #融资
    JcomFinanceStage = scrapy.Field()
    #经纬度
    Jlocation = scrapy.Field()
    #是否为校招
    JisSchoolJob = scrapy.Field()
    #时间
    JcreatedTime = scrapy.Field()
    #来源
    Jsource = scrapy.Field()
    #网站
    Jsite = scrapy.Field()
