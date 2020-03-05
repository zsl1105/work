import pymysql
import xlrd


def read_excel():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='park', charset="utf8")
    curs = conn.cursor()
    sql_insert = "insert into user_park_prize(area,big_detail,company_member,typee,detail_type,prize,prize_money,prize_attach,prize_require)" \
                 " VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    table = xlrd.open_workbook("政策（1218）.xls").sheets()[0]
    for i in range(104, 116):
        area = "浦口高新区"
        big_detail = table.cell(i, 1).value
        company_member = table.cell(i, 2).value
        typee = table.cell(i, 3).value
        detail_type = table.cell(i, 5).value
        prize = table.cell(i, 6).value
        prize_money = str(table.cell(i, 7).value)
        prize_attach = table.cell(i, 8).value
        prize_require = table.cell(i, 9).value
        data = [area, big_detail, company_member, typee, detail_type, prize, prize_money, prize_attach, prize_require]
        print(data)
        curs.execute(sql_insert, data)
        conn.commit()
    conn.close()
    curs.close()


if __name__ == "__main__":
    read_excel()
