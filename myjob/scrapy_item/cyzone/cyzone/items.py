# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CyzoneItem(scrapy.Item):
    name = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    web = scrapy.Field()
    datetime = scrapy.Field()
    stage = scrapy.Field()
    briefs = scrapy.Field()
    company = scrapy.Field()

    phone = scrapy.Field()
    mail = scrapy.Field()
