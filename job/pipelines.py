# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from job.data_cleaning import clean,isTest

class JobPipeline:
    def __init__(self):
        self.db=pymysql.connect(host='47.113.123.159',user='pa',passwd='258258cqu',db='job_info',charset='utf8',port=3306)
        self.cur=self.db.cursor()
    def process_item(self, item, spider):
        # print(item['title'])
        key = item.keys()
        val = item.values()
        dbName ='demo'
        if hasattr(spider, 'Jdb'):
            dbName = spider.Jdb

        item = clean(item)
        if isTest:
            dbName = 'jobclean'
        sql = 'INSERT INTO {}({}) VALUES({})'.format(dbName,','.join(key), ','.join('\''+str(v)+'\'' for v in val))
        # sql='INSERT INTO demo(Jname,Jarea,Jtype,Jrequirements,Jcompany,Jtag,Jwelfare,Jeducation,Jexperience,JminSalary,JmaxSalary,JpayTimes,JcomType,JhireCount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # self.cur.execute(sql, (item['Jname'],
        #     item['Jarea'], item['Jtype'], item['Jrequirements'],
        #     item['Jcompany'], item['Jtag'], item['Jwelfare'],
        #     item['Jeducation'], item['Jexperience'], item['JminSalary'],
        #     item['JmaxSalary'],item['JpayTimes'],item['JcomType'],item['JhireCount']))
        self.cur.execute(sql)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()