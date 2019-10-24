from selenium import webdriver
import time
from lxml import etree
import pymysql
import re


def connect():
    browser = webdriver.Chrome()
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT name FROM startup"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    # print(rows, type(rows))
    # 对数据库进行插入操作，并不需要commit，twisted会自动commit
    insert_sql = 'insert ignore into startup(name,introduction)  VALUES (%s, %s)'
    name_list = []
    for row in rows:
        name_list.append(row[0])
    list = get_html(browser)
    for item in list:
        name = item[0]
        title = item[1]
        if name not in name_list:
            cursor.execute(insert_sql, (name, title))
            conn.commit()
            print(name, title)
            print('***********************')
        else:
            print('%s已经存在！' % name)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_html(browser):
    # browser = webdriver.Chrome()
    url = 'https://36kr.com/information/contact'
    browser.get(url)
    for i in range(3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    for i in range(270):
        print("下拉{}次************".format(i))
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            browser.find_element_by_xpath(
                '//div[contains(@class, "kr-loading-more-button") and contains(@class, "show")]').click()
            time.sleep(3)
        except:
            pass
    response = browser.page_source
    html = etree.HTML(response)
    return get_detail(html)


def get_detail(html):
    title_list = html.xpath('//a[contains(@class, "article-item-title")]')
    list = []
    for item in title_list:
        title = item.text
        pattern = re.compile(r'「(.*?)」')
        poject_name = pattern.findall(title)
        if poject_name:
            name = poject_name[0]
            list.append((name, title))
    return list


connect()
