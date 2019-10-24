import requests
import json
import re
import pymysql


def connect(list):
    conn = pymysql.connect(host='192.168.3.67', user='root', password='123456', port=3306, db='my_test', charset="utf8")
    cursor = conn.cursor()
    select_sql = "SELECT name FROM startup"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    # print(rows, type(rows))a
    # 对数据库进行插入操作，并不需要commit，twisted会自动commit
    insert_sql = 'insert ignore into startup(name,introduction)  VALUES (%s, %s)'
    name_list = []
    for row in rows:
        name_list.append(row[0])
    for item in list:
        name = item[0]
        title = item[1]
        if name not in name_list:
            cursor.execute(insert_sql, (name, title))
            conn.commit()
            print(name, title)
            print('***********************')
        else:
            print('%s已经存在！' % name)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接


def get_html():
    url = 'https://36kr.com/pp/api/feed-stream?type=web&feed_id=305&b_id={}&per_page=30'.format(b_id)
    response = requests.get(url).text
    html = json.loads(response)
    return html


def main():
    global b_id
    while True:
        html = get_html()
        items = html['data']['items']
        next_b_id = items[-1]['id']
        list = []
        for item in items:
            title = item['template_info']['template_title']
            pattern = re.compile(r'「(.*?)」')
            project_name = pattern.findall(title)
            if project_name:
                for i in range(len(project_name)):
                    name = project_name[i]
                    list.append((name, title))

        connect(list)
        b_id = next_b_id


b_id = 401411

main()
