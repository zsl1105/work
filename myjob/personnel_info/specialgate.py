import requests
from lxml import etree
import pymysql
import json


def expertdetails_cn():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    strsql = "Insert into expertdetails_cn(id,name,organization,positionalitles,abstract,focusareas,fund,subjects,email,tel) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for temp in range(95164, 10057):
        try:
            url = 'http://api.specialgate.boguan360.com/api/v1/talants/get/{}'.format(temp)
            print(url)
            response = json.loads(requests.get(url).text)
            name = response["0"]["name"]
            organization = response["0"]["organization"]
            positionalitles = response["0"]["positionalitles"]
            try:
                abstract = "".join(response["0"]["abstract"].split("\n"))
            except:
                abstract = ""
            focusareas = response["0"]["focusareas"][1:-1]
            fund = response["0"]["fund"][1:-1]
            subjects = response["0"]["subjects"][1:-1]
            email = response["0"]["email"]
            tel = response["0"]["tel"]
            dates = [name, organization, positionalitles, abstract, focusareas, fund, subjects, email, tel]
            cursor.execute(strsql, dates)
            conn.commit()
        except:
            pass
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def expertdetails():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    strsql = "Insert into expertdetails(id,authorname, age, organization, countryStr, type_ty, subjects_cn, docnum, quotednum,hindex, subjects,emails) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for temp in range(95164, 114510):
        try:
            url = 'http://api.specialgate.boguan360.com/api/v1/scopus/get/{}'.format(temp)
            print(url)
            response = json.loads(requests.get(url).text)
            # 作者
            authorname = response["0"]["authorname"]
            # 年龄
            age = response["0"]["age"]
            # 组织
            organization = response["0"]["organization"]
            # 国家
            countryStr = response["0"]["countryStr"]
            # 类别
            type_ty = response["0"]["type_ty"]
            # 所属学科
            subjects_cn = response["0"]["subjects_cn"]
            # 发文数量
            docnum = response["0"]["docnum"]
            # 被引次数
            quotednum = response["0"]["quotednum"]
            # h指数
            hindex = response["0"]["hindex"]
            # 课程
            subjects = response["0"]["subjects"]
            # 邮箱
            emails = response["0"]["emails"][1:-1]
            dates = [authorname, age, organization, countryStr, type_ty, subjects_cn, docnum, quotednum,hindex, subjects,emails]
            cursor.execute(strsql, dates)
            conn.commit()
        except Exception as e:
            print(e)
            pass
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


expertdetails()
