from selenium import webdriver
import time
from lxml import etree
import pymysql
import re


def connect():
    browser = webdriver.Chrome()
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cur = conn.cursor()
    sql = "SELECT company FROM startup WHERE id > 36549 and phone IS NULL AND mail IS NULL AND company !='UC' AND company !='HP' AND company !=''"
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    for row in rows:
        company = row[0]
        print('数据库：', company)
        email, phone_number, company_name_result = get_message(company, browser)
        print(email, phone_number, company_name_result)
        print('******************************')
        time.sleep(3)
        if company == company_name_result:
            sql2 = "UPDATE startup SET phone= '%s',mail = '%s' WHERE company = '%s'" % (phone_number, email, company)
            cur.execute(sql2)
            conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_message(company, browser):
    url = 'https://www.qixin.com/search?key=' + company + '&page=1'
    browser.get(url)

    # 判断是否出现登录页面
    # login = browser.find_element_by_class_name('auth-form-container pull-right')
    try:
        login = browser.find_element_by_xpath(
            '//div[contains(@class,"auth-form-container") and contains(@class,"pull-right")]')
        if login:
            time.sleep(60)
    except:
        pass
    # 判断会否出现点击验证码，若有等待十秒手动处理
    # undefined = browser.find_element_by_class_name('btn4')
    try:
        # undefined_onclick = browser.find_element_by_xpath('//div[@class="col-xs-24 error-403 text-center"]/text()')
        undefined_onclick = browser.find_element_by_xpath('//div[contains(@class, "error-403")]')
        if undefined_onclick:
            time.sleep(20)
    except:
        pass
    # 判断会否出现验证码，若有等待十秒手动处理
    # undefined = browser.find_element_by_class_name('btn4')
    try:
        undefined = browser.find_element_by_xpath('//div[@class="btn4"]/text()')
        if undefined:
            if undefined[0] == '点击按钮进行验证':
                time.sleep(20)
    except:
        pass

    response = browser.page_source
    html = etree.HTML(response)

    return detail_parse(html)


def detail_parse(html):
    mail, phone = '', ''
    mail_phones = html.xpath('/html/body/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/span')
    for span in mail_phones:
        span_text = span.text
        if span_text == '邮箱：':
            mail = span.xpath('.//a/text()')[0].strip()
    # pattern = re.compile('<span class="font-f1">电话：</span>(.*?)</span>')
    # phones = pattern.search(str(html).strip())
    # phones = sulu.group(1)
    phones = html.xpath('/html/body/div[2]/div[3]/div/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[4]/span[2]/text()')
    if phones:
        phone = phones[0].strip()

    company_name = html.xpath('//div[contains(@class,"company-title")]')
    if company_name:
        company_name_result = ''.join(company_name[0].xpath('.//a//text()'))
    else:
        company_name_result = ''
    return mail, phone, company_name_result


connect()
