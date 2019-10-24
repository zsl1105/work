import requests
from lxml import etree
import pymysql
import time
import xlrd


def get_html(name, school):
    url = 'https://daoshi.eol.cn/search/index?search_type=4&keyword={}'.format(name)
    print(url)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
    response = requests.get(url, headers).text
    html = etree.HTML(response)
    return get_detail(html, name, school)


def get_detail(html, name, school):
    content_list = html.xpath('//div[@class="td"]')
    for item in content_list:
        name_web = item.xpath('string(.//div[1]/a)').strip()
        info = item.xpath('string(.//div[2])').strip()
        if name == name_web and (info in school or school in info):
            content_url = item.xpath('.//div[6]/a/@class')[0]
            contents_url = 'https://daoshi.eol.cn' + content_url
            return get_content(contents_url)


def get_content(contents_url):
    print(contents_url)
    content_email, content_phone, content_homepage = '', '', ''
    content_personal_profile, content_research_field, content_recent_papers = '', '', ''
    content_response = requests.get(url=contents_url).text
    content_html = etree.HTML(content_response)
    content_list = content_html.xpath('//div[@class="teacher-td"]')
    try:
        content_name_1 = content_list[1].xpath('.//div/a/text()')[0].strip()
        content_name_2 = content_list[1].xpath('string(.)').strip().split('：')[-1]
        content_name_3 = content_list[0].xpath('.//div[1]/text()')[0].strip().split("：")[-1]
        # 姓名
        content_name = str(content_name_1) + str(content_name_2) + content_name_3 + '老师'
        content_title_1 = content_list[2].xpath('.//div[1]/text()')[0].strip().split('：')[-1]
        content_title_2 = content_list[2].xpath('string(.)').strip().split('：')[-1]
        # 职称
        content_title = "{}{}".format(content_title_1, content_title_2)
        content_article = content_html.xpath('//div[@class="lf-item-title"]')
        for content_text in content_article:
            if '通讯方式' in content_text.text:
                content_emails = content_text.getnext().xpath('.//div')
                for email in content_emails:
                    if '电子邮件' in email.text:
                        content_email = email.text.split('：')[1]
            elif '个人简述' in content_text.text:
                content_personal_profile = content_text.getnext().xpath('string(.)').strip()
            elif '科研工作' in content_text.text:
                content_research_field = content_text.getnext().xpath('string(.)').strip()
        dates = [content_name, content_title, content_email, content_personal_profile, content_research_field]
        return dates
    except Exception as e:
        print(e)
        pass


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


def write_mysql():
    is_exit = False
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT name FROM people_info"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    # print(rows, type(rows))
    strsql = "Insert into people_info(id,name,Title,email,baseinfo,project) VALUES (0,%s,%s,%s,%s,%s)"
    # mysql数据
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
                dates = get_html(name, school)
                time.sleep(0.2)
                try:
                    cursor.execute(strsql, dates)
                    conn.commit()
                    print(dates)
                    print('***********************' * 3)
                except Exception as e:
                    print(e)
                    pass
            is_exit = False
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


write_mysql()
