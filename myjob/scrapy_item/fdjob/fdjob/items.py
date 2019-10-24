# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FdjobItem(scrapy.Item):
    company_name = scrapy.Field()
    introduction = scrapy.Field()
