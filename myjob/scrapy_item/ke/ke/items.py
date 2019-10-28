# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KeItem(scrapy.Item):
    name = scrapy.Field()
    company_area = scrapy.Field()
    adress = scrapy.Field()
    start_time = scrapy.Field()
    project = scrapy.Field()
    finance = scrapy.Field()
    company = scrapy.Field()
