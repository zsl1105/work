# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IheimaItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()
    start_time = scrapy.Field()
    phone = scrapy.Field()
    mail = scrapy.Field()
    name = scrapy.Field()
    project = scrapy.Field()
