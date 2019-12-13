# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import re
import time
from dangdang.items import DangdangItem
from scrapy_redis import spiders


class DangbookSpider(spiders.RedisSpider):
    name = 'dangbook'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://e.dangdang.com/list-DZS-dd_sale-0-1.html']

    redis_key = "dangbook:start_urls"

    def parse(self, response):
        first_title_list = response.xpath("//div[contains(@class,'publication')]")
        for first_title in first_title_list:
            first_title_name = first_title.xpath(".//a/h3/@dd_name").extract_first()
            print("一级标题——————", first_title_name)
            for second_title_list in first_title.xpath(".//ul/li"):
                second_title_name = second_title_list.xpath(".//a/h4/@dd_name").extract_first()
                print("二级标题——————", second_title_name)
                for third_title_list in second_title_list.xpath(".//ul/a"):
                    third_title_name = third_title_list.xpath(".//li/@dd_name").extract_first()
                    print("三级标题——————", third_title_name)
                    third_title_type = third_title_list.xpath(".//li/@data-type").extract_first()
                    item = DangdangItem()
                    item["first_title_name"] = first_title_name
                    item["second_title_name"] = second_title_name
                    item["third_title_name"] = third_title_name
                    temp = 0
                    # while temp < 3031:
                    while temp < 100:
                        next_url = "http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&start={}&end={}&category={}&dimension=dd_sale".format(
                            str(temp), str(temp + 20), third_title_type)
                        print("{}采集{}中{}".format("*" * 10, third_title_name, "*" * 10), next_url)
                        if re.search("亲，没有更多内容了", requests.get(next_url).text):
                            print("{}{}已经采集结束{}".format("*" * 10, third_title_name, "*" * 10))
                            break
                        time.sleep(2)
                        yield scrapy.Request(next_url, callback=self.parse_detail, meta={"item": item},
                                             dont_filter=True)
                        temp = temp + 21

    def parse_detail(self, response):
        item = response.meta["item"]
        print(response.url)
        responses = json.loads(response.text)
        for content_list in responses["data"]["saleList"]:
            authorPenname = ''
            try:
                authorPenname = content_list["mediaList"][0]["authorPenname"]
                # print("作者名：", authorPenname)
            except:
                pass
            descs = content_list["mediaList"][0]["descs"]
            # print("简介：", descs)
            title = content_list["mediaList"][0]["title"]
            # print("作品名：", title)
            originalPrice = content_list["mediaList"][0]["originalPrice"]
            # print("原价：", originalPrice)
            lowestPrice = content_list["mediaList"][0]["lowestPrice"]
            # print("促销价：", lowestPrice)
            vipPrice = content_list["mediaList"][0]["vipPrice"]
            # print("VIP价：", vipPrice)
            mediaId = content_list["mediaList"][0]["mediaId"]
            # print("作品ID：", mediaId)
            detail_url = "http://e.dangdang.com/products/{}.html".format(mediaId)
            item["authorPenname"] = authorPenname
            item["descs"] = descs
            item["title"] = title
            item["originalPrice"] = originalPrice
            item["lowestPrice"] = lowestPrice
            item["vipPrice"] = vipPrice
            item["mediaId"] = mediaId
            yield scrapy.Request(detail_url, callback=self.parse_detailPage, meta={"item": item}, dont_filter=True)

    def parse_detailPage(self, response):
        print("{}书籍详情采集{}{}".format("*" * 10, "*" * 10, response.url))
        time.sleep(1)
        item = response.meta["item"]
        try:
            publisher = response.xpath("//p[@id='publisher']/span/a/text()").extract_first()
            publish_date = \
            response.xpath("//p[@id='publisher']/following-sibling::p[1]/text()").extract_first().split("：")[
                1]
            content_num = \
            response.xpath("//p[@id='publisher']/following-sibling::p[2]/text()").extract_first().split("：")[
                1]
            content_score = response.xpath("//div[@class='count_per']/em[2]/text()").extract_first()
            item["publisher"] = publisher
            item["publish_date"] = publish_date
            item["content_num"] = content_num
            item["content_score"] = content_score
            yield item
        except:
            pass
