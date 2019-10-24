import requests

url = 'https://daoshi.eol.cn/tutor/40980'
headers = {
    "Host": "www.x-mol.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Referer": "https://www.x-mol.com/university/searchTutor/simple?option=%E5%BC%A0%E6%9C%AA%E5%8D%BF",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "UM_distinctid=16c6afdc67d952-000029b8a7ae03-c343162-1fa400-16c6afdc67e6f1; PAPER_COOKIE_ACADEMIC_AREA_KEY=1; Hm_lvt_543e8bb9e2ec1a0b9400d55857a600b0=1565163111,1565163245; closeFloatWindow=true; WAPSESSIONID=a23b318e-e6bb-4a17-8f6e-de8ee633602b; CNZZDATA1262978740=614804173-1565161339-https%253A%252F%252Fwww.baidu.com%252F%7C1565314173; Hm_lpvt_543e8bb9e2ec1a0b9400d55857a600b0=1565318887",
}
print(requests.get(url=url).text)
