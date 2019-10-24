import requests

url = "https://fdjob.bjx.com.cn/Companys.shtml"
print(requests.get(url).content.decode("gbk"))
