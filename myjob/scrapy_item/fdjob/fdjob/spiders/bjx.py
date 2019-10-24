# -*- coding: utf-8 -*-
import scrapy
from fdjob.items import FdjobItem
import xlrd


class BjxSpider(scrapy.Spider):
    name = 'bjx'
    allowed_domains = ['bix.com.cn']
    start_urls = ['https://fdjob.bjx.com.cn/Companys.shtml']

    def parse(self, response):
        n = 0
        name_list = []
        # print(response.text)
        item = FdjobItem()
        company_list = response.xpath("//div[contains(@class,'project_mb9')]")[1:-1]
        for temps in company_list:
            company_content_list = temps.xpath(".//div[2]/ul/li")
            for temp in company_content_list:
                company_name = temp.xpath(".//a/text()").extract()[0]
                company_url = 'https://fdjob.bjx.com.cn' + temp.xpath(".//a/@href").extract()[0]
                print(company_url)
                data = xlrd.open_workbook(r'栖霞区-智慧能源.xlsx')
                for table in data.sheets():
                    for i in range(table.nrows):  # 有效行
                        name = table.cell(i, 1).value
                        name_list.append(name)
                if company_name not in name_list:
                    n = n + 1
                    print(n)
                    item["company_name"] = company_name
                    yield scrapy.Request(company_url, callback=self.parse_d, meta={"item": item}, dont_filter=True)

    def parse_d(self, response):
        print(response)
        item = response.meta["item"]
        company_introduction = response.xpath("//div[@class='bjx-comIntro']/div[2]")
        introduction = ''
        for p in company_introduction.xpath('.//p/text()'):
            introduction = introduction + p.extract().strip()
        item["introduction"] = introduction
        yield item
