import pymysql
import xlrd


def read_excel():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    curs = conn.cursor()
    sql_insert = "insert into 2019_CONTEST_FINAL_LIST(id,name,background,gender,degree,project,email,phone,area)" \
                 " VALUE (0,%s,%s,%s,%s,%s,%s,%s,%s)"
    tables = xlrd.open_workbook("江苏行项目汇总.xlsx")
    for table in tables.sheets():
        for i in range(2, table.nrows):
            # 名字
            name = table.cell(i, 1).value
            # 海外背景
            background = table.cell(i, 2).value
            # 学历
            gender = table.cell(i, 3).value
            # 性别
            degree = table.cell(i, 4).value
            # 项目
            project = table.cell(i, 5).value
            # 邮箱
            email = table.cell(i, 6).value
            # 电话
            phone = table.cell(i, 7).value
            # 所属领域
            area = table.cell(i, 8).value
            data = [name, background, gender, degree, project, email, phone, area]
            curs.execute(sql_insert, data)
            conn.commit()
    conn.close()
    curs.close()


if __name__ == "__main__":
    read_excel()
