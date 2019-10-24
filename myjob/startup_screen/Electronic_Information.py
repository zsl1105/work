import pymysql
import xlwt

workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('Electronic_Information')
conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
cursor = conn.cursor()
select_sql = "SELECT * FROM `startup` WHERE area='文化创意' AND (start_time LIKE '2017%' or start_time LIKE '2018%' OR start_time LIKE '2019%')"
cursor.execute(select_sql)
rows = cursor.fetchall()
n = 0
for row in rows:
    for col in range(len(row)):
        worksheet.write(n, col, row[col])
    print('*' * 8)
    n = n + 1
workbook.save('11.xls')
