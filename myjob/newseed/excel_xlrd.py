# import xlrd
#
# Workbook = xlrd.open_workbook("aaa.xlsx")
# Workbook_2 = xlrd.open_workbook("bbb.xlsx")
# mysheet = Workbook.sheet_by_index(0)
# myColValues = mysheet.col_values(0)
# mysheet_2 = Workbook_2.sheet_by_index(0)
# myColValues_2 = mysheet_2.col_values(0)
# # n = 0
# for temp in myColValues:
#


import requests

url = "http://www.cnzsyz.com/aozhou/info/426226.html"
print(requests.get(url))

response = requests.get(url)
response.encoding = "GBK"
html = response.text
print(html)
