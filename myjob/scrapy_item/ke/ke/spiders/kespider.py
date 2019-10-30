# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from ke.items import KeItem
from ke.settings import COOKIES
import random


class KespiderSpider(scrapy.Spider):
    name = 'kespider'
    allowed_domains = ['rong.36ke.com']
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    }
    cookeis = COOKIES[0]
    # industry_list = ["E_COMMERCE", "SOCIAL_NETWORK", "INTELLIGENT_HARDWARE", "MEDIA", "SOFTWARE",
    #                  "CONSUMER_LIFESTYLE",
    #                  "FINANCE", "MEDICAL_HEALTH", "SERVICE_INDUSTRIES", "TRAVEL_OUTDOORS",
    #                  "PROPERTY_AND_HOME_FURNISHINGS", "EDUCATION_TRAINING", "AUTO", "LOGISTICS", "AI", "UAV",
    #                  "ROBOT",
    #                  "VR_AR", "SPORTS", "FARMING", "SHARE_BUSINESS", "CHU_HAI", "CONSUME"]
    # phase_list = ["SEED", "ANGEL", "PRE_A", "A", "A_PLUS", "PRE_B", "B", "B_PLUS", "C", "C_PLUS", "D", "E",
    #               "INFORMAL", "PRIVATE_REPLACEMENT"]

    industry_list = ["E_COMMERCE", "SOCIAL_NETWORK", ]
    phase_list = ["SEED", "ANGEL", ]

    def start_requests(self):
        for industry in self.industry_list:
            for phase in self.phase_list:
                for i in range(5, 6 ):
                    try:
                        url = "https://rong.36kr.com/n/api/column/0/company?phase={}&industry={}&sortField=HOT_SCORE&p={}".format(
                            phase, industry, str(i))
                        yield scrapy.Request(url=url, headers=self.headers, cookies=self.cookeis, callback=self.parse,
                                             dont_filter=True)
                    except Exception as e:
                        print("出现错误：", e)

    def parse(self, response):
        if response.status == 200:
            data = json.loads(response.text)
            for i in range(20):
                company_id = data['data']['pageData']['data'][i]['id']
                company_area = data['data']['pageData']['data'][i]['industryStr']
                item = KeItem()
                print(company_id)
                url = "https://rong.36kr.com/n/api/company/{}?asEncryptedTs=0.042819194793378985&asTs=1571729062861".format(
                    company_id)
                print(url)
                yield scrapy.Request(url=url, headers=self.headers, cookies=self.cookeis, callback=self.detail_parse,
                                     meta={'item': item, 'company_area': company_area},
                                     dont_filter=True)

    def detail_parse(self, response):
        print(response.url)
        item = response.meta['item']
        company_data = json.loads(response.text)
        # 项目名字
        name = company_data["data"]["name"]
        item['name'] = name
        # 领域
        item['company_area'] = response.meta['company_area']
        # 地址
        adress = company_data["data"]["address1Desc"]
        item['adress'] = adress
        # 创立时间
        try:
            start_time = company_data["data"]["startDateDesc"]
            item['start_time'] = start_time
        except:
            item['start_time'] = ''
        # 项目简介
        project = company_data["data"]["intro"]
        item['project'] = project
        # 融资历史
        finance = company_data["data"]["projectStatHeader"]["phase"]
        item['finance'] = finance
        # 公司全称
        company = company_data["data"]["fullName"]
        item['company'] = company
        print(item)
        yield item
