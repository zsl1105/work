import requests
import xlwt, xlrd
from lxml import etree


# name area company project finance introduction mail phone
def get_content(url):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf8')
    # 创建工作表
    worksheet = workbook.add_sheet('Information')
    n = 0
    response = requests.get(url).text
    html = etree.HTML(response)
    content_list = html.xpath('//div[@class="table-responsive"]/table/tbody/tr')
    for content in content_list:
        name = content.xpath("string(.//td[1])")
        area = content.xpath("string(.//td[2])")
        company = content.xpath("string(.//td[3])")
        project = content.xpath("string(.//td[4])")
        finance = content.xpath("string(.//td[5])")
        introduction = content.xpath("string(.//td[6])")
        mail = content.xpath("string(.//td[7])")
        phone = content.xpath("string(.//td[8])")
        row = [name, area, company, project, finance, introduction, mail, phone]
        for col in range(len(row)):
            worksheet.write(n, col, row[col])
        print('*' * 8)
        n = n + 1
    workbook.save('aa.xls')


def main1():
    aa = '数字创意产业'
    url = "http://192.168.3.67:8000/search/?csrfmiddlewaretoken=kcbGqKUD4kma1fB6UVYH2nYI2OU0rrSYe8WtQLDKNOPnitoHih85Uv7gzEg9UbYs&q={}".format(
        aa)
    get_content(url)


main1()
