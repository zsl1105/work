# -*- coding: utf-8 -*-
import scrapy


class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = ['jingdata.com']
    start_urls = ['http://jingdata.com/']

    def parse(self, response):
        pass
