# -*- coding: utf-8 -*-
import scrapy
from cyzone.items import CyzoneItem
from lxml import etree
import requests
import time


class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = ['www.cyzone.cn']
    start_urls = ['https://www.cyzone.cn/company/list-0-0-859-0-0/0']

    def parse(self, response):
        item = CyzoneItem()
        content_list = response.xpath('//tr[contains(@class,"table-plate") and contains(@class, "item")]')
        next_url_list = response.xpath('//*[@id="pages"]/a')
        for content in content_list:
            name = content.xpath('.//td[2]/a/span/text()')
            stage = content.xpath('.//td[3]/a/text()')
            area = content.xpath('.//td[4]/a/text()')
            datetime = content.xpath('.//td[5]//text()')
            content_url = content.xpath('.//td[2]/a/@href')
            try:
                if name:
                    name = name[0].extract().strip()
                if stage:
                    stage = stage[0].extract().strip()
                if area:
                    area = area[0].extract().strip()
                if datetime:
                    datetime = datetime[0].extract().strip()
                if content_url:
                    content_urls = 'https:' + content_url[0].extract().strip()
                    print(content_urls)
                    result_response = requests.get(content_urls).text
                    time.sleep(3)
                    html = etree.HTML(result_response)
                    company, web, address, briefs = next_parse(html)
                    item['name'] = name
                    item['stage'] = str(stage)
                    item['area'] = str(area)
                    item['datetime'] = str(datetime)
                    item['company'] = str(company)
                    item['web'] = str(web)
                    item['address'] = str(address)
                    item['briefs'] = str(briefs)
                    yield item
            except Exception as e:
                print(e)
                pass

        for next_url in next_url_list:
            if next_url.xpath('.//text()').extract()[0] == '下一页':
                result_next_url = next_url.xpath('.//@href').extract()[0]
                result_next_url = 'https://www.cyzone.cn' + result_next_url
                print(result_next_url)

                yield scrapy.Request(result_next_url, callback=self.parse, dont_filter=True)


def next_parse(html):
    company = html.xpath('//*[@id="main"]/div[3]/div[1]/ul/li[2]/text()')
    web = html.xpath('//*[@id="main"]/div[3]/div[1]/ul/li[3]/div/a/@href')
    address = html.xpath('//*[@id="main"]/div[4]/div/div[2]/div[1]/div[1]/ul/li[2]/span/text()')
    brief = html.xpath('//div[@class="info-box"]//text()')

    try:
        if len(''.join(company).strip()) != 0:
            company = ''.join(company).strip().split('：')[1]
        else:
            company = ''
        if web:
            web = ''.join(web).strip()
        else:
            web = ''
        if address:
            address = ''.join(address).strip()
        else:
            address = ''
        if brief:
            briefs = ''.join(brief).strip()
        else:
            briefs = ''
        return company, web, address, briefs
    except Exception as e:
        print(e)
        pass
