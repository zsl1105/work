import requests
from lxml import etree
import time
import xlrd
import xlutils.copy
import pymysql


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
        time.sleep(10)

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
        'Cookie': 'aliyungf_tc=AQAAAMrPWUaCPAAAH9dZdUG+7/QqsstZ; csrfToken=LsRel-mH7ZZbNfsjyGV4YGr8; jsid=SEM-BAIDU-PZ2003-SY-000001; TYCID=2d13d75064d811ea83e79bca78875764; undefined=2d13d75064d811ea83e79bca78875764; ssuid=9465567595; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1584069022; _ga=GA1.2.2107357143.1584069023; bannerFlag=true; _gid=GA1.2.173061172.1584317639; RTYCID=479c326776e84cc69d2fce1775f79d09; CT_TYCID=125145ddec554d7a847a4c0680575624; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522schoolGid%2522%253A%2522%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522254%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTk5MzIwODY0NSIsImlhdCI6MTU4NDMyOTMxNiwiZXhwIjoxNjE1ODY1MzE2fQ.rMi4Sd-X RVtIEEVOS7NqAFEoxgFGb8vLzkZ3VkfQU1-WeiO2bhG2ly8R06tII2l4_CMMYeioHAD0Xzu57z-7Xw%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%2589%25BE%25E5%25B0%25BC%25E7%25BB%25B4%25E4%25BA%259A%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522companyGid%2522%253A%2522%2522%252C%2522mobile%2522%253A%252215993208645%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTk5MzIwODY0NSIsImlhdCI6MTU4NDMyOTMxNiwiZXhwIjoxNjE1ODY1MzE2fQ.rMi4Sd-XRVtIEEVOS7NqAFEoxgFGb8vLzkZ3VkfQU1-WeiO2bhG2ly8R06tII2l4_CMMYeioHAD0Xzu57z-7Xw; tyc-user-phone=%255B%252215993208645%2522%252C%2522182%25200369%25203349%2522%255D; _gat_gtag_UA_123487620_1=1; token=611faa0c2b844782b2ea6ce3eea1b628; _utm=d61fbf30063e4096b0a35c128fa27926; cloud_token=e682d212eb8446cc9db5a31cb5ac9938; cloud_utm=2984ef0db0d74ded8fdbbb5308819864; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1584329321'
    }

    response = requests.request("GET", url, headers=headers, data=payload).text
    return response


def from_excel():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT company_name FROM `guogaoxin` WHERE phone is NULL and email is NULL"
    strsql = "Insert into guogaoxin(phone, email, web, address, introduction, registered_capital, paid_capital, date, state,credit_code, registered_number, indentity_number, organization_code, company_type, area,approval_date, registration_authority, business_term, taxpayer_qualification,personnel_scale, insured_persons, name_used_before, english_name, business_scope) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    for row in rows:
        company_name = row[0]

        # 切换企查查或天眼查api
        # 企查查 result = get_message(company_name)
        # 天眼查 result = get_message_tianyan(company_name)
        result = get_message_tianyan(company_name)
        if '高新技术企业' in result[0]:
            print("{}是高新技术企业".format(company_name))
            # 企查查url  company_url = "https://www.qichacha.com" + result[1]
            # 天眼查url ompany_url = result[1]
            company_url = result[1]
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
                # 电话
                phone = \
                    html_detail.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[1]/span[2]/text()')
                if phone:
                    phone = phone[0].strip()
                else:
                    phone = ''
                # 邮箱
                email = \
                    html_detail.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[2]/span[2]/text()')
                if email:
                    email = email[0].strip()
                else:
                    email = ''
                # 网站
                web = html_detail.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[1]/a/text()')
                if web:
                    web = web[0].strip()
                else:
                    web = ''
                # 地址
                address = \
                    html_detail.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/text()')
                if address:
                    address = address[0].strip()
                else:
                    address = ''
                # 简介
                introduction = html_detail.xpath('//*[@id="company_base_info_detail"]//text()')
                if introduction:
                    introduction = introduction[0].strip()
                else:
                    introduction = ''
                # 注册资本
                registered_capital = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[1]/td[2]//text()')[0].strip()
                # 实缴资本
                paid_capital = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[1]/td[4]//text()')[
                    0].strip()
                # 成立日期
                date = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[2]/td[2]//text()')[
                    0].strip()
                # 经营状态
                state = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[2]/td[4]//text()')[
                    0].strip()
                # 统一社会信用代码
                credit_code = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[3]/td[2]//text()')[
                    0].strip()
                # 工商注册号
                registered_number = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[3]/td[4]//text()')[0].strip()
                # 纳税人识别号
                indentity_number = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[4]/td[2]//text()')[0].strip()
                # 组织机构代码
                organization_code = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[4]/td[4]//text()')[0].strip()
                # 公司类型
                company_type = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[5]/td[2]//text()')[
                    0].strip()
                # 行业
                area = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[5]/td[4]//text()')[
                    0].strip()
                # 核准日期
                approval_date = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[6]/td[2]//text()')[
                    0].strip()
                # 登记机关
                registration_authority = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[6]/td[4]//text()')[0].strip()
                # 营业期限
                business_term = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[7]/td[2]//text()')[
                    0].strip()
                # 纳税人资质
                taxpayer_qualification = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[7]/td[4]//text()')[0].strip()
                # 人员规模
                personnel_scale = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[8]/td[2]//text()')[0].strip()
                # 参保人数
                insured_persons = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[8]/td[4]//text()')[0].strip()
                # 曾用名
                name_used_before = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[9]/td[2]//text()')[0].strip()
                # 英文名
                english_name = html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[9]/td[4]//text()')[
                    0].strip()
                # 经营范围
                business_scope = \
                    html_detail.xpath('//*[contains(@class,"-border-top-none")]/tbody/tr[11]/td[2]//text()')[0].strip()
                strsql = "update guogaoxin set phone= '%s',email='%s',web='%s',address='%s',introduction='%s',registered_capital='%s',paid_capital='%s',date='%s',state='%s',credit_code='%s',registered_number='%s',indentity_number='%s',organization_code='%s',company_type='%s',area='%s',approval_date='%s',registration_authority='%s',business_term='%s',taxpayer_qualification='%s',personnel_scale='%s',insured_persons='%s',name_used_before='%s',english_name='%s',business_scope='%s' where company_name = '%s'" % (
                    phone, email, web, address, introduction, registered_capital, paid_capital, date, state,
                    credit_code, registered_number, indentity_number, organization_code, company_type, area,
                    approval_date, registration_authority, business_term, taxpayer_qualification, personnel_scale,
                    insured_persons, name_used_before, english_name, business_scope, company_name)

                cursor.execute(strsql)
                conn.commit()
            except Exception as e:
                print("爬取到**{}**时候出错,出错信息：{}".format(company_name, e))
                time.sleep(10)
                pass
        else:
            sql_2 = 'DELETE FROM guogaoxin WHERE company_name="{}"'.format(company_name)
            cursor.execute(sql_2)
            conn.commit()
            print("已删除***{}***".format(company_name))
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


from_excel()
