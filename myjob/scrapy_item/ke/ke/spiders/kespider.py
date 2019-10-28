# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from ke.items import KeItem


class KespiderSpider(scrapy.Spider):
    oble = False
    name = 'kespider'
    allowed_domains = ['rong.36ke.com']
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    }
    cookeis = {
        'kr_stat_uuid': 'kwWWS26064183',
        'device-uid': '4442aef0-b723-11e9-84b5-639540c9b49f',
        'download_animation': '1',
        'krnewsfrontss': '3583db26833583b5e4e715e5248353fe',
        'M-X SRF-TOKEN': 'f36de0663a9f2fa96262335cd2208ecdd4ce2d2fa2f00d7ce91bfb76324a5a6f',
        'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1569544443,1571383333,1571618227',
        'Hm_lvt_1684191ccae0314c6254306a8333d090': '1569544443,1571383333,1571618227',
        'ktm_source': 'kaike_pclandingpage',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22kwWWS26064183%22%2C%22%24device_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%7D',
        'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1571618311',
        'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1571618311',
        'Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3': '1571618356',
        'Hm_lpvt_e8ec47088ed7458ec32cde3617b23ee3': '1571618356',
        ' _kr_p_se': 'c663ef9c-5185-414e-841e-8f8f6005fc22',
        'krid_user_id': '941851778',
        ' krid_user_version': '2',
        'kr_plus_id': '941851778',
        'kr_plus_token': '3sYTEv7AwXzMT6Iii6znd8JijrYmEt76844_____',
    }
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
                for i in range(1, 3):
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
