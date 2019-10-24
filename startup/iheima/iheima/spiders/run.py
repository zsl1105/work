# -*- coding: utf-8 -*-
import scrapy
from iheima.items import IheimaItem
import json
import time


class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = ['iheima.com']

    # start_urls = ['http://www.iheima.com/enterprise-library/detail/40294']

    def start_requests(self):
        url = 'http://www.iheima.com/enterprise-library/detail/{}'
        for i in range(200000, 300000):
            yield scrapy.Request(url.format(i), dont_filter=False)

    def parse(self, response):
        print('主页的url:', response.url)
        phone, mail = '', ''
        html = response.text
        # 公司名字
        company = response.xpath('//div[@class="enterprise-desc"]/h3/text()').extract_first()
        # 分类
        title = response.xpath('//div[@class="enterprise-desc"]/ul/li[1]/text()').extract_first().replace(' ',
                                                                                                          '').strip()
        # 成立时间
        start_time = response.xpath('//div[@class="enterprise-desc"]/ul/li[3]/text()').extract_first().split('：')[-1]

        for i in response.xpath('.//div[@class="block-content"]/p'):
            i_name = i.xpath('string(.)').extract_first()
            if '电话' in i_name:
                # 电话
                phone = i_name.split('：')[-1]
            if '邮箱' in i_name:
                # 邮箱
                mail = i_name.split('：')[-1].replace('\xa0', '')
        item = IheimaItem()
        item["company"] = company
        item["title"] = title
        item["start_time"] = start_time
        item["phone"] = phone
        item["mail"] = mail
        temp = response.url.split('/')[-1]
        product_base_url = 'http://www.iheima.com/enterprise-library/product/{}'.format(temp)
        headers = {"X-Requested-With": "XMLHttpRequest"}
        yield scrapy.Request(product_base_url, headers=headers, meta={"item": item}, callback=self.product_parse,
                             dont_filter=False)

    def product_parse(self, response):
        # 打印项目详情页url
        print('产品页的URL：', response.url.replace('product', 'detail'))
        item = response.meta['item']
        content_list = json.loads(response.text)['data']['list']
        if content_list:
            for content in content_list:
                name = content['name']
                project = content['detail']
                item["name"] = name
                item["project"] = project
                # print(item)
                yield item
