import requests
import xlrd
from lxml import etree
from selenium import webdriver
import time
import re
import pymysql


def get_html(browser, name, school):
    url = 'http://www.chinamaven.com'
    browser.get(url)
    browser.find_element_by_name('title').clear()
    time.sleep(1)
    browser.find_element_by_name('title').send_keys(name)
    time.sleep(1)
    browser.find_element_by_id('submit').click()
    time.sleep(1)
    response = browser.page_source
    html = etree.HTML(response)
    return get_detail(html, name, school)


def get_detail(html, name, school):
    url_list = html.xpath('//*[@id="waterfall"]/li')
    # time.sleep(1)
    for url in url_list:
        try:
            people_info = url.xpath('.//div[2]/a//text()')[0]
            if name in people_info and school in people_info:
                content_url = url.xpath('.//div[1]/a/@href')[0]
                contents_url = 'http://www.chinamaven.com/' + content_url
                return get_content(contents_url)
        except:
            pass


def get_content(contents_url):
    baseinfo = ''
    paper = ''
    project = ''
    other = ''
    print(contents_url)
    response = requests.get(contents_url).text
    response = response.replace('<br>', '\n')
    HTML = etree.HTML(response)
    name = HTML.xpath('//*[@id="ct"]/div[1]/div[1]/div/h2/text()')[0].strip()
    # print("名字：", name)
    zc = HTML.xpath('//*[@id="ct"]/div[1]/ul[1]/li[1]/text()')[0].strip()
    title = zc.split('：')[-1]
    # print("职称：", title)
    area = HTML.xpath('//*[@id="ct"]/div[1]/ul[1]/li[2]/a[1]/text()')[0].strip()
    # print('地区：', area)
    zhuanye_1 = HTML.xpath('//*[@id="ct"]/div[1]/ul[1]/li[3]/a[1]/text()')[0].strip()
    zhuanye_2 = HTML.xpath('//*[@id="ct"]/div[1]/ul[1]/li[3]/a[2]/text()')[0].strip()
    major = zhuanye_1 + '-' + zhuanye_2
    # print('专业：', major)
    result_email = HTML.xpath('//*[@id="ct"]/div[1]/ul[1]/li[4]/text()')[0].strip()
    if result_email.split('：')[0] == '邮箱':
        email = result_email.split('：')[1]
    else:
        email = ''
    # print('邮箱：', email)
    info = HTML.xpath('//ul[@class="tb mtw cl"]')
    for item in info:
        info_title = item.xpath('.//li/a/text()')[0]
        if info_title == '基本信息':
            baseinfo = item.getnext().xpath('string(.)')
            rel_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", baseinfo)
            if rel_email:
                email = rel_email[0]
                # print('邮箱：', email)
            # print('基本信息：', baseinfo)
        if info_title == '论文著作':
            paper = item.getnext().xpath('string(.)')
            # print('论文著作：', paper)
        if info_title == '做过的课题或项目':
            project = item.getnext().xpath('string(.)')
            # print('做过的课题或项目：', project)
        if info_title == '其它':
            other = item.getnext().xpath('string(.)')
            rel_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", other)
            if rel_email:
                email = rel_email[0]
                # print('邮箱：', email)
            # print('其他：', other)
    date = [name, title, area, major, email, baseinfo, paper, project, other]
    return date


def read_excel():
    is_exit = False
    browser = webdriver.Chrome()
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT name FROM people"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    # print(rows, type(rows))
    strsql = "Insert into people VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    name_list = []
    for row in rows:
        name_list.append(row[0])

    data = xlrd.open_workbook(r'万人计划.xlsx')
    for table in data.sheets():
        for i in range(table.nrows):  # 有效行
            # time.sleep(2)
            name = table.cell(i, 1).value
            school = table.cell(i, 2).value
            for item in name_list:
                if name in item:
                    is_exit = True
                    print('%s已经存在！' % name)
                    break
            if not is_exit:
                date = get_html(browser, name, school)
                try:
                    cursor.execute(strsql, date)
                    conn.commit()
                    print(date)
                    print('***********************' * 3)
                except Exception as e:
                    print(e)
                    pass
            is_exit = False
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_old_info():
    dates = []
    for line in open('千人计划1-5.txt', 'r', encoding='utf8'):
        if '：' in line:
            name = line.split('：')[0].strip()
            company = line.split('：')[1].strip()
            dates.append((name, company))
        elif ' ' in line:
            names = line.rsplit(' ', 1)[0]
            name = ''.join(names.split())
            company = line.rsplit(' ', 1)[1].strip()
            dates.append((name, company))
    return dates


read_excel()
