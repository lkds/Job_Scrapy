# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JobPipeline:
    def __init__(self):
        self.db=pymysql.connect(host='47.113.123.159',user='pa',passwd='258258cqu',db='job_info',charset='utf8',port=3306)
        self.cur=self.db.cursor()
    def process_item(self, item, spider):
        # print(item['title'])
        sql='INSERT INTO demo(Jname,Jsalary,Jarea,Jtype,Jrequirements,Jcompany,Jtag,Jwelfare,Jeducation,Jexperience,JminSalary,JmaxSalary,JpayTimes,JcomType) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cur.execute(sql, (item['Jname'], item['Jsalary'],
            item['Jarea'], item['Jtype'], item['Jrequirements'],
            item['Jcompany'], item['Jtag'], item['Jwelfare'],
            item['Jeducation'], item['Jexperience'], item['JminSalary'],
            item['JmaxSalary'],item['JpayTimes'],item['JcomType']))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()