import xlrd
import xlutils.copy

totle_list = []
data = xlrd.open_workbook(r'C:\Users\92375\Desktop\初创项目\startup.xlsx')
data_1 = xlrd.open_workbook(r'C:\Users\92375\Desktop\初创项目\2019contest.xlsx')
ws = xlutils.copy.copy(data_1)
table_2 = ws.get_sheet(0)
table = data.sheets()[0]
table_1 = data_1.sheets()[0]
for i in range(0, table.nrows):  # 有效行
    totle_list.append(table.cell(i, 2).value)

for i in range(0, table_1.nrows):  # 有效行
    if table_1.cell(i, 3).value in totle_list:
        table_2.write(i, 2, '已存在')
ws.save(r'C:\Users\92375\Desktop\初创项目\2019contest.xlsx')