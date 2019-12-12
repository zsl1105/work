# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    first_title_name = scrapy.Field()
    second_title_name = scrapy.Field()
    third_title_name = scrapy.Field()
    authorPenname = scrapy.Field()
    descs = scrapy.Field()
    title = scrapy.Field()
    originalPrice = scrapy.Field()
    lowestPrice = scrapy.Field()
    vipPrice = scrapy.Field()
    mediaId = scrapy.Field()
    publisher = scrapy.Field()
    publish_date = scrapy.Field()
    content_num = scrapy.Field()
    content_score = scrapy.Field()


