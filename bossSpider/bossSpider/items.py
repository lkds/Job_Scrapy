'''
@Descripttion: 
@version: 
@Author: Paul
@Date: 2020-06-29 17:12:23
@LastEditors: Paul
@LastEditTime: 2020-06-29 17:18:15
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Jname = scrapy.Field()
    Jsalary = scrapy.Field()
    Jarea = scrapy.Field()
    Jtype = scrapy.Field()
    Jrequirements = scrapy.Field()
    Jcompany = scrapy.Field()
