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
        headers = {
            # "Connection": "keep-alive",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Referer": "http://e.dangdang.com/list-QGDS-dd_sale-0-1.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "__permanent_id=20191210093457020296006400993333375; ddscreen=2; MDD_channelId=70000; MDD_fromPlatform=307; pos_1_end=1575965008243; pos_1_start=1575965014550; pos_9_end=1575965053513; pos_6_end=1575965053628; pos_6_start=1575965057028; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23sp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fZ-jkY0kyKh0KGwAsaj5OKI000000n7yNC00000IN-r1L%7C%230-%7C-; __ddc_1d=1576025991%7C\u0021%7C_utm_brand_id%3D11106; __ddc_24h=1576025991%7C\u0021%7C_utm_brand_id%3D11106; __ddc_15d=1576025991%7C\u0021%7C_utm_brand_id%3D11106; __ddc_15d_f=1576025991%7C\u0021%7C_utm_brand_id%3D11106; __rpm=mix_317715...1575965087836%7Cmix_824776...1576025999710; bookName=%u72C4%u516C%u6848%2C%u5C0F%u8BF4%2C%u514D%u8D39; bookTotal=21; producthistoryid=1900694833%2C1900778799%2C1901154024%2C1900547280%2C1900694666%2C1900625628%2C1901119185%2C1900544980%2C1901139335%2C1901086409; __visit_id=20191211171401177443009658808764978; __out_refer=; __trace_id=20191211171955416557284813687318452",
        }
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
                        try:
                            next_url = "http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&start={}&end={}&category={}&dimension=dd_sale".format(
                                str(temp), str(temp + 20), third_title_type)
                            print("{}采集{}中{}".format("*" * 10, third_title_name, "*" * 10), next_url)
                            if re.search("亲，没有更多内容了", requests.get(next_url).text):
                                print("{}{}已经采集结束{}".format("*" * 10, third_title_name, "*" * 10))
                                break
                            time.sleep(2)
                            yield scrapy.Request(next_url, callback=self.parse_detail, headers=headers, meta={"item": item},
                                                 dont_filter=True)
                            temp = temp + 21
                        except Exception as e:
                            print("$"*10+"连接断开，抛出异常"+"$"*10+"\n",e)
                            pass

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
            time.sleep(1)
            yield scrapy.Request(detail_url, callback=self.parse_detailPage, meta={"item": item}, dont_filter=True)

    def parse_detailPage(self, response):
        print("{}书籍详情采集{}{}".format("*" * 10, "*" * 10, response.url))
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
