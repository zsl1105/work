# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os


class DangdangPipeline(object):
    def __init__(self):
        csvfile = os.path.dirname(__file__) + '/spiders/articles.csv'
        self.file = open(csvfile, 'a+', encoding="utf8", newline='')
        self.writer = csv.writer(self.file, dialect="excel")

    def process_item(self, item, spider):
        # print("pipelines___________{}".format(item))
        if item["first_title_name"]:
            self.writer.writerow(
                [item['first_title_name'], item['second_title_name'], item['third_title_name'], item['authorPenname'],
                 item['title'], item['descs'], item['originalPrice'], item['lowestPrice'], item['vipPrice'],
                 item['mediaId'],
                 item['publisher'], item['publish_date'], item['content_num'], item['content_score']])
        return item

    def close_spider(self, spider):
        self.file.close()
