import requests
from lxml import etree
import pymysql
import xlrd
import time


def get_html(name, school):
    url = 'https://www.x-mol.com/university/searchTutor/simple?option={}'.format(name)
    print(url)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
    response = requests.get(url, headers).text
    html = etree.HTML(response)
    return get_detail(html, name, school)


def get_detail(html, name, school):
    content_list = html.xpath('//div[@class="teacher-search-list"]/a')
    for item in content_list:
        name_web = item.xpath('string(.//li/div[2]/span[1])').strip()
        info = item.xpath('normalize-space(.//li/div[2])').strip()
        if name == name_web and school in info:
            content_url = item.xpath('.//@href')[0]
            contents_url = 'https://www.x-mol.com/' + content_url
            return get_content(contents_url)


def get_content(contents_url):
    print(contents_url)
    content_email, content_phone, content_homepage = '', '', ''
    content_personal_profile, content_research_field, content_recent_papers = '', '', ''
    headers = {
        "Host": "www.x-mol.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://www.x-mol.com/university/searchTutor/simple?option=%E5%BC%A0%E6%9C%AA%E5%8D%BF",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "UM_distinctid=16c6afdc67d952-000029b8a7ae03-c343162-1fa400-16c6afdc67e6f1; PAPER_COOKIE_ACADEMIC_AREA_KEY=1; Hm_lvt_543e8bb9e2ec1a0b9400d55857a600b0=1565163111,1565163245; closeFloatWindow=true; WAPSESSIONID=a23b318e-e6bb-4a17-8f6e-de8ee633602b; CNZZDATA1262978740=614804173-1565161339-https%253A%252F%252Fwww.baidu.com%252F%7C1565314173; Hm_lpvt_543e8bb9e2ec1a0b9400d55857a600b0=1565318887",
    }
    content_response = requests.get(url=contents_url, headers=headers).text
    content_html = etree.HTML(content_response)
    content_list = content_html.xpath('//div[@class="teacher-list-detail-info-right"]/span')
    try:
        content_name = str(''.join(content_list[-1].text.strip().split())) + str(content_list[0].text.strip()) + '老师'
        content_title = content_list[1].text.strip()
        content_detail_info = content_html.xpath('//div[@class="teacher-detail-info-contact"]/li')
        for content in content_detail_info:
            content_text = content.text.strip()
            if '邮箱' in content_text:
                content_email = content_text.split('：')[-1]
            elif '电话' in content_text:
                content_phone = content_text.split('：')[-1]
            elif '主页' in content_text:
                content_homepage = content.xpath('.//a/text()')[0].strip()
        content_article = content_html.xpath('//article[@class="teacher-list-detail-article"]')
        for artice in content_article:
            text = artice.xpath('.//h3/text()')[0].strip()
            if '个人简介' in text:
                content_personal_profile = artice.xpath('string(.)').strip()
            if '研究领域' in text:
                content_research_field = artice.xpath('string(.)').strip()
            if '近期论文' in text:
                content_recent_papers = artice.xpath('string(.)').strip()
        dates = [content_name, content_title, content_email, content_personal_profile, content_research_field,
                 content_recent_papers]
        return dates
    except Exception as a:
        print(a)
        pass


def write_mysql():
    is_exit = False
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT name FROM people_info"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    # print(rows, type(rows))
    strsql = "Insert into people_info(id,name,Title,email,baseinfo,project,other) VALUES (0,%s,%s,%s,%s,%s,%s)"
    # mysql数据
    name_list = []
    for row in rows:
        name_list.append(row[0])
    data = xlrd.open_workbook(r'万人计划.xlsx')
    for table in data.sheets():
        for i in range(table.nrows):  # 有效行
            time.sleep(2)
            name = table.cell(i, 1).value
            school = table.cell(i, 2).value
            for item in name_list:
                if name in item:
                    is_exit = True
                    print('%s已经存在！' % name)
                    break
            if not is_exit:
                dates = get_html(name, school)
                # time.sleep(2)
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
