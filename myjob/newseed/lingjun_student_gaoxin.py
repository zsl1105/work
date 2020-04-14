import requests
from lxml import etree
import time
import xlrd
import xlutils.copy


def get_message(company_name):
    url = "https://www.qcc.com/search?key=" + str(company_name)
    print(url)
    response = get_detail(url)
    # time.sleep(3)
    html = etree.HTML(response)
    try:

        company_tage = html.xpath('//*[@class="search-tags"]')[0].xpath('.//text()')
        company_url = html.xpath('//*[@class="ma_h1"]')[0].xpath('.//@href')[0]

    except Exception as e:
        print("爬取到**{}**时候出错,出错信息：{}".format(company_name, e))
        company_tage = ''
        company_url = ''

    return company_tage, company_url


def get_detail(url):
    payload = {}
    headers = {
        'authority': 'www.qcc.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'referer': 'https://www.qcc.com/firm_b4979ec34257f828def41b182e631226.html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'acw_tc=7518031d15832224314912858ea41e503f79f078a5217c1534b18425b0; QCCSESSID=k14q6e77vablhi0a3rrrqeske6; zg_did=%7B%22did%22%3A%20%22170d15debf99ea-074e1943fb38bb-2393f61-1cb7b9-170d15debfa8e%22%7D; UM_distinctid=170d15decf1df-02217b35b01299-2393f61-1cb7b9-170d15decf24e8; CNZZDATA1254842228=59307857-1584060074-https%253A%252F%252Fwww.qichacha.com%252F%7C1584060074; Hm_lvt_78f134d5a9ac3f92524914d0247e70cb=1584060559,1584061079,1584061095; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201584060558335%2C%22updated%22%3A%201584061900640%2C%22info%22%3A%201584060558338%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22f2ee63125cfe56de35a2f1d798bb6771%22%7D; Hm_lpvt_78f134d5a9ac3f92524914d0247e70cb=1584061901'
    }

    response = requests.request("GET", url, headers=headers, data=payload).text
    # print(response)
    return response


def get_message_tianyan(company_name):
    url = "https://www.tianyancha.com/search?key=" + str(company_name)
    print(url)
    response = get_detail_tianyan(url)
    # time.sleep(1)
    html = etree.HTML(response)
    try:

        company_tage = html.xpath('//div[contains(@class,"sv-search-company")]')[0].xpath('.//text()')
        company_url = html.xpath('//a[contains(@class, "name")]')[0].xpath('.//@href')[0].strip()

    except Exception as e:
        print("爬取到**{}*时候出错,出错信息：{}".format(company_name, e))
        company_tage = ''
        company_url = ''
        pass
        # time.sleep(10)

    return company_tage, company_url


def get_detail_tianyan(url):
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'https://www.tianyancha.com/company/2349349655',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'TYCID=2d13d75064d811ea83e79bca78875764; undefined=2d13d75064d811ea83e79bca78875764; ssuid=9465567595; _ga=GA1.2.2107357143.1584069023; jsid=SEM-BAIDU-PZ2003-VI-000001; bad_id658cce70-d9dc-11e9-96c6-833900356dc6=caffa391-6f41-11ea-b1ba-df6758fc5b10; aliyungf_tc=AQAAANVrF0ZZjwwAl5ButNG/yTfX2dUx; csrfToken=5o6kwI_5_5uWFMXkVj5M9z4U; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1584069022,1585202083,1585633737,1585704858; _gid=GA1.2.1959156277.1586218902; RTYCID=7ac89ba65c6a46909280943c3d5b075a; CT_TYCID=ed2d8c2804d645118e87feaf47250de1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522schoolGid%2522%253A%2522%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25222%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMzY5MzM0OSIsImlhdCI6MTU4NjMwODIwMiwiZXhwIjoxNjE3ODQ0MjAyfQ.QL12R1tPFilgi1GACO2qy0anJezTerCH6-V_lI11CHM6UHXo7NShLdSKKsY4YnrA49Glu0rp4M9WLbZHnYjuxA%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25AE%258B%25E5%2593%25B2%25E5%25AE%2597%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522companyGid%2522%253A%2522%2522%252C%2522mobile%2522%253A%252218203693349%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODIwMzY5MzM0OSIsImlhdCI6MTU4NjMwODIwMiwiZXhwIjoxNjE3ODQ0MjAyfQ.QL12R1tPFilgi1GACO2qy0anJezTerCH6-V_lI11CHM6UHXo7NShLdSKKsY4YnrA49Glu0rp4M9WLbZHnYjuxA; tyc-user-phone=%255B%252218203693349%2522%252C%2522159%25209320%25208645%2522%255D; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1586309484; token=a56863517a214da793a0f49221583e59; _utm=82dc73aeb99240e5b74064bfb42ff344; cloud_token=8b8dee4f161c4f94ad934b343ca97eec; cloud_utm=bcd9fee14d3b4e76bceebb9cfca88bde'
    }

    response = requests.request("GET", url, headers=headers, data=payload).text
    return response


def from_excel():
    data = xlrd.open_workbook(r'E:\省人才和企业落户政策\20200331.xls')
    ws = xlutils.copy.copy(data)
    table_2 = ws.get_sheet(0)
    table = data.sheets()[0]
    for i in range(1, table.nrows):  # 有效行
        if not table.cell(i, 26).value:
            company_name = table.cell(i, 17).value
            # 切换企查查或天眼查api
            # 企查查 result = get_message(company_name)
            # 天眼查 result = get_message_tianyan(company_name)
            result = get_message_tianyan(company_name)

            company_url = result[1]
            if company_url:
                # 切换企查查或天眼查api
                # 企查查 response_detail = get_detail(company_url)
                # 天眼查 response_detail = get_detail_tianyan(company_url)
                response_detail = get_detail_tianyan(company_url)
                html_detail = etree.HTML(response_detail)
                # 公司经营范围  //*[@id="_container_baseInfo"]/table[2]/tbody/tr[11]
                #              //*[@id="_container_baseInfo"]/table[2]/tbody/tr[11]/td[2]/span/text()
                try:
                    # 切换企查查或天眼查api
                    # 企查查 company_scope = html_detail.xpath('//*[@id="_container_baseInfo"]/table/tr')[-1].xpath('.//td[2]//text()')[0].strip()
                    # 天眼查 company_scope = html_detail.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr')[-1].xpath('.//td[2]//text()')[0].strip()
                    # 经营状态
                    company_state = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[2]/td[4]//text()')[0].strip()
                    # 司法风险
                    legal_proceedings = html_detail.xpath('//div[@nav-id="nav_nav-main-lawDangerous"][1]/a//text()')[-1].strip()
                    # 经营风险
                    business_risk = html_detail.xpath('//div[@nav-id="nav_nav-main-manageDangerous"][1]/a//text()')[-1].strip()
                    print("经营状态**{}**,司法风险**{}**经营风险**{}**".format(company_state,legal_proceedings,business_risk))
                except Exception as e:
                    print("爬取到**{}**时候出错,出错信息：{}".format(company_name, e))
                    company_state = ''
                    legal_proceedings = ''
                    business_risk = ''
                    # time.sleep(10)
                    pass
                table_2.write(i, 26, company_state)
                table_2.write(i, 27, legal_proceedings)
                table_2.write(i, 28, business_risk)
                ws.save(r'E:\省人才和企业落户政策\20200331.xls')


from_excel()
