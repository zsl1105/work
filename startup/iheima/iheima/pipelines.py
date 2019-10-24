# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class IheimaPipeline(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item


from .settings import MY_SETTINGS
from pymysql import cursors
from twisted.enterprise import adbapi
import copy


class IheimaPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        asyn_mysql_settings = MY_SETTINGS
        asyn_mysql_settings['cursorclass'] = cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        # dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        item = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # print(item)
        select_sql = "SELECT name FROM startup"
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        # print(rows, type(rows))
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = 'insert ignore into startup(title, name,start_time, phone, mail, project, company) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        name_list = []
        for row in rows:
            name_list.append(row['name'])

        if item['name'] not in name_list:
            if item['start_time'] > '2010-00-00':
                cursor.execute(insert_sql, (item['title'], item['name'], item['start_time'], item['phone'],
                                            item['mail'], item['project'], item['company']))
                print(item)
                print('***********************')
            else:
                print('%s时间太久了！，时间为%s' % (item['name'], item['start_time']))
        else:
            print('%s已经存在！' % item['name'])

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)
