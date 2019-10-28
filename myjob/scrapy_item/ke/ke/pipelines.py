# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

pymysql.install_as_MySQLdb()


class KePipeline(object):
    # def __init__(self):
    #     self.client = pymysql.connect(
    #         host='132.232.52.243',
    #         port=3306,
    #         user='zhanshunlong',
    #         passwd='gaoxun123',
    #         db='91boshi',
    #         charset='utf8'
    #     )
    #     self.cor = self.client.cursor()

    def __init__(self):
        self.client = pymysql.connect(
            host='192.168.3.67',
            port=3306,
            user='root',
            passwd='123456',
            db='my_test',
            charset='utf8'
        )
        self.cor = self.client.cursor()

    def process_item(self, item, spider):
        sql = 'insert into startup(name,area,address,start_time,project,finance,company) VALUES ' \
              '(%s,%s,%s,%s,%s,%s,%s)'
        lis = (item['name'], item['company_area'], item['adress'], item['start_time'], item['project'], item['finance'],
               item['company'])
        self.cor.execute(sql, lis)
        self.client.commit()
        print("存入！！！！")
        return item

