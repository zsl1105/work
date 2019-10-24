import requests

url = 'https://xiangmu.trjcn.com/list_1.html?y=3007'
print(requests.get(url).text)
