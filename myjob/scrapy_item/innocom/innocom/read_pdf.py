import os.path
import pdfplumber
import pandas as pd
import pymysql


def read_pdf():
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    strsql = "Insert into guogaoxin(company_name) VALUES (%s)"

    filepath = 'D:\work\myjob\scrapy_item\innocom\innocom\pdf_sum'
    pathdir = os.listdir(filepath)
    for alldir in pathdir:
        child = os.path.join('%s\%s' % (filepath, alldir))
        print('新文件:::',child)
        if os.path.isfile(child):
            with pdfplumber.open(child) as pdf:
                for page in pdf.pages:
                    print("爬到{}PDF文件，第{}页".format(child,page.page_number))
                    tables = page.extract_tables()
                    for table in tables:
                        df = pd.DataFrame(table[:])[1]
                        try:
                            if not df[3]:
                                df = pd.DataFrame(table[:])[3]
                        except:
                            pass
                        for company_name in df:
                            if company_name in ['企业名称','']:
                                continue
                            print("存入***{}***".format(company_name))
                            cursor.execute(strsql, company_name)
                            conn.commit()
        os.remove(child)
        print("删除{}文件".format(child))
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


read_pdf()
