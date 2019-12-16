import redis
import pymysql
import json


def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    # 指定mysql数据库信息
    mysqlcli = pymysql.Connect(host='127.0.0.1', user='root', passwd='123456', db='my_test', port=3306,
                               use_unicode=True)

    while True:
        source, data = rediscli.blpop(["dangbook:items"])
        item = json.loads(data)
        try:
            cur = mysqlcli.cursor()
            data = [item["first_title_name"], item["second_title_name"], item["third_title_name"],
                    item["authorPenname"],
                    item["descs"], item["title"], item["originalPrice"], item["lowestPrice"], item["vipPrice"],
                    item["mediaId"], item["publisher"], item["publish_date"], item["content_num"],
                    item["content_score"]]
            sql = "INSERT INTO dangdang(first_title_name, second_title_name, third_title_name, authorPenname, descs, title, originalPrice, lowestPrice, vipPrice, mediaId, publisher, publish_date, content_num, content_score) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, data)
            mysqlcli.commit()
            cur.close()
        except Exception as e:
            print("出现错误！！！", e)


main()
