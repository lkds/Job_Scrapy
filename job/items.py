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
    Jsalary =scrapy.Field()
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
