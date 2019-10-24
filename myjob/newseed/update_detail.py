import pymysql
import requests
from lxml import etree
import time
from urllib.request import quote
import random

cookie_pool = [
    'zg_did=%7B%22did%22%3A%20%2216c1ca141c1617-09550b960486d2-c343162-1fa400-16c1ca141c25a5%22%7D; UM_distinctid=16c1ca141f5a00-05d12ebb23ae5-c343162-1fa400-16c1ca141f6c3d; _uab_collina=156384842619376764127956; acw_tc=3da0cc9c15638484077493420ee5d1898bcca5beb5dffd2dd5f3a651cc; QCCSESSID=0q3d1a3mr6bvfp0018ouiag735; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1564984678,1564987178,1565052656,1565061964; hasShow=1; CNZZDATA1254842228=1052502065-1563845986-https%253A%252F%252Fwww.baidu.com%252F%7C1565165113; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1565167587; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201565167510618%2C%22updated%22%3A%201565167590040%2C%22info%22%3A%201565061963382%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%228bd106ee9e7476c0a5d4072a55f719d9%22%7D',
    'zg_did=%7B%22did%22%3A%20%2216c1ca141c1617-09550b960486d2-c343162-1fa400-16c1ca141c25a5%22%7D; UM_distinctid=16c1ca141f5a00-05d12ebb23ae5-c343162-1fa400-16c1ca141f6c3d; _uab_collina=156384842619376764127956; acw_tc=3da0cc9c15638484077493420ee5d1898bcca5beb5dffd2dd5f3a651cc; QCCSESSID=0q3d1a3mr6bvfp0018ouiag735; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1564984678,1564987178,1565052656,1565061964; hasShow=1; CNZZDATA1254842228=1052502065-1563845986-https%253A%252F%252Fwww.baidu.com%252F%7C1565165113; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1565167637; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201565167510618%2C%22updated%22%3A%201565167638584%2C%22info%22%3A%201565061963382%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%225aad4bd32ec9706a3ae56750a60b8dc4%22%7D',
    'zg_did=%7B%22did%22%3A%20%2216c1ca141c1617-09550b960486d2-c343162-1fa400-16c1ca141c25a5%22%7D; UM_distinctid=16c1ca141f5a00-05d12ebb23ae5-c343162-1fa400-16c1ca141f6c3d; _uab_collina=156384842619376764127956; acw_tc=3da0cc9c15638484077493420ee5d1898bcca5beb5dffd2dd5f3a651cc; QCCSESSID=0q3d1a3mr6bvfp0018ouiag735; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1564984678,1564987178,1565052656,1565061964; hasShow=1; CNZZDATA1254842228=1052502065-1563845986-https%253A%252F%252Fwww.baidu.com%252F%7C1565165113; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1565167689; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201565167510618%2C%22updated%22%3A%201565167695084%2C%22info%22%3A%201565061963382%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22bc5df723803134604728392ac78f5620%22%7D',
    ]


def connect():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cur = conn.cursor()
    sql = 'SELECT name FROM startup WHERE company="BitX" and phone="-" and name !="Yo"'
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    for row in rows:
        time.sleep(3)
        name = row[0]
        print('数据库：', name)
        try:
            company_name, phone, mail, company_product = get_message(name)
            print(company_name, phone, mail, company_product)
            print('***********************')
            if name.upper() == company_product.upper():
                sql2 = 'UPDATE startup SET phone= "%s",mail = "%s",company = "%s" WHERE name = "%s"' % (
                phone, mail, company_name, name)
                cur.execute(sql2)
                conn.commit()
            else:
                sql3 = 'UPDATE startup SET phone= "--",mail = "--" WHERE name = "%s"' % (name)
                cur.execute(sql3)
                conn.commit()
        except:
            pass
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_message(name):
    url = "https://www.qichacha.com/search?key=" + str(name)
    response = get_detail(url)
    html = etree.HTML(response)
    company_name = html.xpath('//*[@id="search-result"]/tr[1]/td[3]/a//text()')
    if company_name:
        company_name = ''.join(company_name)
    else:
        company_name = ''
    phone = html.xpath('//tbody[@id="search-result"]/tr/td[3]/p[2]/span/text()')
    if phone:
        phone = phone[0].split('：')[1].strip()
    else:
        phone = ''
    # print(phone)
    mail = html.xpath('//tbody[@id="search-result"]/tr/td[3]/p[2]/text()')
    if mail:
        mail = mail[0].split('：')[1].strip()
    else:
        mail = None
    # print(mail)
    company_product = html.xpath('//*[@id="search-result"]/tr[1]/td[3]/p[4]//text()')
    if company_product:
        company_product = ''.join(company_product).strip().split('：')[1]
    else:
        company_product = ''
    return company_name, phone, mail, company_product


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
        "Cookie": random.choice(cookie_pool)
    }
    reponses = requests.get(url, headers=headers)
    html = reponses.text
    return html


connect()
