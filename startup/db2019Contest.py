import xlrd
import pymysql


def read_sum_sheets():
    conn = pymysql.connect(host='132.232.52.243', user='zhanshunlong', password='gaoxun123', db='91boshi',
                           charset='utf8')
    cursor = conn.cursor()
    strsql = "Insert into 2019Contest(id,area,startup_name,startup_sort,company_name,startup_intro,startup_history," \
             "company_intro,email,phone) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = xlrd.open_workbook(r'信息汇总.xls')
    for book in data.sheets():
        # sheet名字(领域)
        area = book.name
        for row in range(1, book.nrows):
            # 项目名
            startup_name = book.cell(row, 0).value
            # 分类
            startup_sort = book.cell(row, 1).value
            # 公司名
            company_name = book.cell(row, 2).value
            # 项目介绍
            startup_intro = book.cell(row, 3).value
            # 融资历史
            startup_history = book.cell(row, 4).value
            # 公司简介
            company_intro = book.cell(row, 5).value
            # 邮箱
            email = book.cell(row, 6).value
            # 电话
            phone = book.cell(row, 7).value
            startup_value_list = [area, startup_name, startup_sort, company_name, startup_intro, startup_history,
                                  company_intro, email, phone]
            cursor.execute(strsql, startup_value_list)
            conn.commit()
            print(startup_name)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def read_2019contest():
    conn = pymysql.connect(host='132.232.52.243', user='zhanshunlong', password='gaoxun123', db='91boshi',
                           charset='utf8')
    cursor = conn.cursor()
    strsql = "Insert into 2019Contest(id,area,startup_name,startup_sort,company_name,startup_intro,startup_history," \
             "company_intro,email,phone) VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = xlrd.open_workbook(r'海外留学创业项目1.xlsx')
    for book in data.sheets():
        for row in range(1, book.nrows):
            # sheet名字(领域)
            area = book.cell(row, 5).value
            # 项目名
            startup_name = book.cell(row, 0).value
            # 公司名
            company_name = book.cell(row, 1).value
            # 项目介绍
            startup_intro = book.cell(row, 2).value
            # 邮箱
            email = book.cell(row, 3).value
            # 电话
            phone = book.cell(row, 4).value
            startup_value_list = [area, startup_name, '', company_name, startup_intro, '', '', email, phone]
            cursor.execute(strsql, startup_value_list)
            conn.commit()
            print(startup_name)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


read_2019contest()
