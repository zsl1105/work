import requests
import xlwt, xlrd, re
from lxml import etree
import time


def get_qichacha(company):
    time.sleep(1)
    start_time = ''
    print(company)
    url = 'https://www.qichacha.com/search?key={}'.format(company)
    headers = {
        "Host": "www.qichacha.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://www.qichacha.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Cookie": "zg_did=%7B%22did%22%3A%20%2216c1ca141c1617-09550b960486d2-c343162-1fa400-16c1ca141c25a5%22%7D; UM_distinctid=16c1ca141f5a00-05d12ebb23ae5-c343162-1fa400-16c1ca141f6c3d; _uab_collina=156384842619376764127956; QCCSESSID=t8a2o3m9o4jq60d4jf1rr66706; CNZZDATA1254842228=1549769987-1567648705-https%253A%252F%252Fsp0.baidu.com%252F%7C1567648705; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1567653240; acw_tc=3da0cc9515676532414514735e4a04e4c638b0ea7d481ea217cade9317; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201567653239872%2C%22updated%22%3A%201567653457581%2C%22info%22%3A%201567653239881%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22sp0.baidu.com%22%2C%22cuid%22%3A%20%22bc5df723803134604728392ac78f5620%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1567653458"
    }
    reponses = requests.get(url, headers=headers)
    html = reponses.text
    pat = re.compile(r'<span class="m-l">成立日期：(.*?)</span>')
    start_time1 = pat.findall(html)
    if start_time1:
        start_time = start_time1[0]
    return start_time


# print(get_qichacha('长沙博为软件技术股份有限公司'))

def read():
    content_values = []
    xl = xlrd.open_workbook(r'C:\Users\92375\Desktop\新建文件夹\信息汇总.xls')
    sheet1 = xl.sheet_by_name('数字创意产业')
    rows = sheet1.nrows
    for row in range(rows):
        content_values.append(sheet1.row_values(row)[0])
    return content_values


def get_content(url):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf8')
    # 创建工作表
    worksheet = workbook.add_sheet('Information')
    n = 0
    response = requests.get(url).text
    html = etree.HTML(response)
    content_list = html.xpath('//div[@class="table-responsive"]/table/tbody/tr')
    for content in content_list:
        name = content.xpath("string(.//td[1])")
        area = content.xpath("string(.//td[2])")
        company = content.xpath("string(.//td[3])")
        project = content.xpath("string(.//td[4])")
        finance = content.xpath("string(.//td[5])")
        introduction = content.xpath("string(.//td[6])")
        mail = content.xpath("string(.//td[7])")
        phone = content.xpath("string(.//td[8])")
        row = [name, area, company, project, finance, introduction, mail, phone]
        print(row)
        boole_value = False
        start_time = ''
        content_values = read()
        if name not in content_values:
            for ro in row:
                if ('2016' in ro) or ('2017' in ro) or ('2018' in ro) or ('2019' in ro):
                    boole_value = True
                    print('获得有效成立时间变量置为：{}'.format(boole_value))
                    continue
            if not boole_value:
                start_time = get_qichacha(company)
                print('从企查查里获得成立时间：{}'.format(start_time))
            if boole_value or ('2016' in start_time) or ('2017' in start_time) or ('2018' in start_time) or (
                    '2019' in start_time):
                print("获得条件符合数据************")
                for col in range(len(row)):
                    worksheet.write(n, col, row[col])
                print('********数据存入{}条******************'.format(n + 1))
                n = n + 1
    workbook.save('22.xls')


aa = '文化创意'
url = "http://192.168.3.67:8000/search/?csrfmiddlewaretoken=kcbGqKUD4kma1fB6UVYH2nYI2OU0rrSYe8WtQLDKNOPnitoHih85Uv7gzEg9UbYs&q={}".format(
    aa)
get_content(url)
