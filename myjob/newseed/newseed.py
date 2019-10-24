import requests
from lxml import etree
import math, time
import pymysql


def get_content_url():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cur = conn.cursor()
    # 先用一个页面测试
    for num in range(178, 190):
        # for num in range(181, 182):
        url = 'https://www.newseed.cn/project/f' + str(num)
        response = requests.get(url).text
        print(response)
        html = etree.HTML(response)
        title = html.xpath('//div[@class="crumbs"]/ul/li[4]/span/text()')
        if title:
            title = title[0]
        print("领域：", title)
        sum_page = html.xpath('//div[@class="search-box-main"]/div[8]/div[1]/span[1]/span/text()')[0]
        for item in range(1, math.ceil(int(sum_page) / 10) + 1):
            rel_url = url + '-p' + str(item)
            print("翻页网址：", rel_url)
            rel_response = requests.get(rel_url).text
            rel_html = etree.HTML(rel_response)
            content_list = rel_html.xpath('//table[@class="table-list"]/tbody/tr')
            # time.sleep(2)
            get_detail_url(content_list, title, cur, conn)

    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_detail_url(content_list, title, cur, conn):
    for tr in content_list:
        content_url = tr.xpath('.//td[1]/a/@href')
        if content_url:
            content_rel_url = content_url[0]
            print(content_rel_url)
            # time.sleep(1)
            rel_content_response = requests.get(content_rel_url).text
            rel_content_html = etree.HTML(rel_content_response)
            content_list = analysis_content(rel_content_html)
            if content_list:
                content_list.insert(0, title)
                content_list.insert(0, 0)
                print("整合的内容：", content_list)
                sql = "insert into startup(id,title, name, area, platform, " \
                      "address, web, start_time, state, project, finance, introduction, company) " \
                      "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, content_list)
                conn.commit()  # 对于数据增删改之后一定要提交操作


def analysis_content(rel_content_html):
    project = ''
    company = ''
    name = rel_content_html.xpath('//h1[@class="title"]/text()')[0]
    # print("项目名：", name)
    area = rel_content_html.xpath('//ul[@class="subinfo"]/li[1]/p[1]/a/text()')[0]
    # print("领域：", area)
    result_platform = rel_content_html.xpath('//ul[@class="subinfo"]/li[1]/p[2]/span[1]/text()')[0]
    platform = result_platform.split("：")[-1]
    # print("平台：", platform)
    result_address = rel_content_html.xpath('//ul[@class="subinfo"]/li[1]/p[2]/span[2]/text()')[0]
    address = result_address.split("：")[-1]
    # print("坐标：", address)
    result_web = rel_content_html.xpath('//ul[@class="subinfo"]/li[1]/p[3]/span/text()')[0]
    web = result_web.split("：")[-1]
    # print("官网：", web)
    result_start_time = rel_content_html.xpath('//ul[@class="subinfo"]/li[2]/p[1]/text()')[0]
    start_time = result_start_time.split("：")[-1]
    # print("成立时间：", start_time)
    result_state = rel_content_html.xpath('//ul[@class="subinfo"]/li[2]/p[2]/text()')[0]
    state = result_state.split("：")[-1]
    # print("运营状态：", state)
    projecta = rel_content_html.xpath('//div[@id="desc"]/div//text()')
    projectb = rel_content_html.xpath('//div[@id="desc"]/div/div//text()')
    if projecta:
        project = projecta[0]
    elif projectb:
        project = projectb[0]
    else:
        project = ''
    # print("项目介绍：", project)
    finance = rel_content_html.xpath('string(//table[@class="record-table"])')
    if finance:
        finance = finance
    else:
        finance = ''
    # print("融资历史：", finance)
    introduction = rel_content_html.xpath('//dd[@class="desc"]//text()')
    if introduction:
        introduction = introduction[0]
    else:
        introduction = ''
    # print("公司简介：", introduction)
    company_url = rel_content_html.xpath('//h4[@class="title"]/a/@href')
    if company_url:
        rel_company_url = company_url[0].strip()
        rel_company_response = requests.get(rel_company_url).text
        rel_company_html = etree.HTML(rel_company_response)
        company_name = rel_company_html.xpath('//div[@class="info-box"]/div[1]/div[2]/p[1]/text()')
        if company_name:
            company = company_name[0].split('\xa0\xa0\xa0\xa0\xa0\xa0')[0]
    company_m = rel_content_html.xpath('//table[@class="base-info"]/tr[1]/td[2]/a/text()')
    if company_m:
        company = company_m[0].split(' ')[0]
    company_l = rel_content_html.xpath('//div[@id="company-box"]/div/dl/p/a/text()')
    if company_l:
        company = company_l[0]

    print("公司名字：", company, type(company))
    content_list = [name, area, platform, address, web, start_time, state, project, finance, introduction, company]
    print(len(content_list))
    if len(company) == 0:
        return content_list


get_content_url()
