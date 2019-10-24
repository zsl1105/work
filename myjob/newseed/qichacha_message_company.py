import pymysql
import requests
from lxml import etree
import time
import csv


def connect():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cur = conn.cursor()
    sql = 'SELECT company FROM startup WHERE id  > 1912480 and phone ="" AND mail ="" AND company !="UC" AND company !="HP" AND company !=""'
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    for row in rows:
        company_name = str(row).split('\'')[1]
        print(company_name)
        try:
            pass
            # phone, mail = get_message(company_name)
        except:
            pass
        print("****************************************")
        sql2 = "UPDATE startup SET phone= '%s',mail = '%s' WHERE company = '%s'" % (phone, mail, company_name)
        cur.execute(sql2)
        conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_message(company_name):
    url = "https://www.qichacha.com/search?key=" + str(company_name)
    print(url)
    response = get_detail(url)
    time.sleep(2)
    html = etree.HTML(response)
    result_company_name = html.xpath('//tbody[@id="search-result"]/tr[1]/td[3]/a//text()')
    if result_company_name:
        result_company_name = ''.join(result_company_name).strip()
    else:
        result_company_name = ''
    print("公司名字：", result_company_name)
    adress = html.xpath('//*[@id="search-result"]/tr[1]/td[3]/p[3]//text()')
    if adress:
        adress = ''.join(adress).split('：')[1].strip()
    else:
        adress = ''
    print("地址：", adress)
    capital = html.xpath('//*[@id="search-result"]/tr[1]/td[3]/p[1]/span[1]/text()')
    if capital:
        capital = capital[0].split('：')[1].strip()
    else:
        capital = ''
    print("注册资本：", capital)
    date = html.xpath('//*[@id="search-result"]/tr[1]/td[3]/p[1]/span[2]/text()')
    if date:
        date = date[0].split('：')[1].strip()
    else:
        date = ''
    print("成立日期：", date)
    phone = html.xpath('//tbody[@id="search-result"]/tr/td[3]/p[2]/span/text()')
    if phone:
        phone = phone[0].split('：')[1].strip()
    else:
        phone = ''
    print("电话：", phone)
    mail = html.xpath('//tbody[@id="search-result"]/tr/td[3]/p[2]/text()')
    if mail:
        mail = mail[0].split('：')[1].strip()
    else:
        mail = ''
    print("邮箱：", mail)
    content_list = [result_company_name, adress, capital, date, phone, mail]
    return content_list


def get_detail(url):
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
        "Cookie": "zg_did=%7B%22did%22%3A%20%2216c1ca141c1617-09550b960486d2-c343162-1fa400-16c1ca141c25a5%22%7D; UM_distinctid=16c1ca141f5a00-05d12ebb23ae5-c343162-1fa400-16c1ca141f6c3d; _uab_collina=156384842619376764127956; QCCSESSID=hv11seuadltua9qhvdii9hbbc1; acw_tc=7518019f15706967126457063ee6ba820bbcace5ae8671fc8fc3c759a6; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1571208478,1571208720,1571209352,1571210002; hasShow=1; CNZZDATA1254842228=348830830-1570692237-%7C1571287916; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1571291176; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201571290902526%2C%22updated%22%3A%201571291177335%2C%22info%22%3A%201570696712232%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%221f4ae9a57aafa575d352cf6c32ec14bc%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D"
    }
    reponses = requests.get(url, headers=headers)
    html = reponses.text
    return html


def read_write_csv():
    with open("bjx.csv", "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            company_name = row[0]
            content_list = get_message(company_name)
            write_csv(content_list)


def write_csv(content_list):
    with open("aaa.csv", "a+", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(content_list)


read_write_csv()
