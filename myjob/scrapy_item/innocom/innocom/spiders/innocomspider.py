# -*- coding: utf-8 -*-
import scrapy
import requests


class InnocomspiderSpider(scrapy.Spider):
    name = 'innocomspider'
    allowed_domains = ['innocom.gov.cn']

    # start_urls = ['http://innocom.gov.cn/']

    def start_requests(self):

        for i in range(1, 15):
            url = "http://www.innocom.gov.cn/gxjsqyrdw/rdba/list_{}.shtml".format(str(i))
            if i == 1:
                url = "http://www.innocom.gov.cn/gxjsqyrdw/rdba/list.shtml"
            print(url)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        content_list = response.xpath('//div[@class="list7"]/ul/li')
        for content in content_list:
            content_url = 'http://www.innocom.gov.cn' + content.xpath('.//a/@href').extract_first()
            print('content_url:',content_url)
            yield scrapy.Request(url=content_url, callback=self.detail_parse, dont_filter=True)

    def detail_parse(self, response):
        content_detail_name = response.xpath('//div[@id="content"]')[-1].xpath('.//a/text()').extract_first()
        content_detail_url = '/'.join(response.url.split('/')[0:-1]) + '/' + response.xpath('//div[@id="content"]').xpath('.//a/@href').extract_first()
        print('content_detail_url:',content_detail_url)
        r = requests.get(content_detail_url)
        with open('./pdf_sum/{}.pdf'.format(content_detail_name), 'wb+') as f:
            f.write(r.content)
            f.close()











