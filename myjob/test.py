import requests
from lxml import etree

url = "https://www.newseed.cn/invest/f178-r20-a185-p2"

# querystring = {"sortField": "HOT_SCORE", "p": "1"}
#
# headers = {
#
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
#
#     'cookie': "kr_stat_uuid=kwWWS26064183; device-uid=4442aef0-b723-11e9-84b5-639540c9b49f; download_animation=1; krnewsfrontss=3583db26833583b5e4e715e5248353fe; M-X SRF-TOKEN=f36de0663a9f2fa96262335cd2208ecdd4ce2d2fa2f00d7ce91bfb76324a5a6f; Hm_lvt_713123c60a0e86982326bae1a51083e1=1569544443,1571383333,1571618227; Hm_lvt_1684191ccae0314c6254306a8333d090=1569544443,1571383333,1571618227; ktm_source=kaike_pclandingpage; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22kwWWS26064183%22%2C%22%24device_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1571618311; Hm_lpvt_1684191ccae0314c6254306a8333d090=1571618311; Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3=1571618356; Hm_lpvt_e8ec47088ed7458ec32cde3617b23ee3=1571618356; _kr_p_se=c663ef9c-5185-414e-841e-8f8f6005fc22; krid_user_id=941851778; krid_user_version=2; kr_plus_id=941851778; kr_plus_token=3sYTEv7AwXzMT6Iii6znd8JijrYmEt76844_____",
#
# }

response = requests.get(url).text

html = etree.HTML(response)
result_list = html.xpath('/html/body/div[3]/div/div[3]/tr')[1:-1]
print(result_list)
for item in result_list:
    company_name = item.xpath('.//td[@class = "td2"]/span[1]//text()')[0]
    print(company_name)
