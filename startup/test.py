import json
import requests

url = "http://www.iheima.com/enterprise-library/product/75"

headers = {
    'Cookie': "DH_MM_ID=eznU711KLbp8pTYLA1RKAg==; _WX=vmmsu4mjicf8blgpg77k85d340; _csrf=01c2525a1051db91e8c684d82d3f0258114939aa86dc4e1aae65a5bca62ac23da^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22IQrvGkpRs8lbFuUR6KzY1RfFBtU9l91I^%^22^%^3B^%^7D; PHPSESSID=vdvhr8nvefo5f40369buufb8o3; Hm_lvt_74c7e2842e192eb6e87dd32cdcfcb60f=1566971446; Hm_lpvt_74c7e2842e192eb6e87dd32cdcfcb60f=1566971446; nb-referrer-hostname=www.iheima.com; nb-start-page-url=http^%^3A^%^2F^%^2Fwww.iheima.com^%^2Fcollege^%^2Fshiyanshi^%^3Ffm^%^3DBDSEM6^%^26renqun_youhua^%^3D1849731; BAIDU_SSP_lcr=https://www.baidu.com/link?url=bpMb4DLRHpTfxtAla5HqxHCBm_nlZ8Go4PVNnjQZVdi^&wd=^&eqid=db06facc002a5a06000000045d661935; Hm_lvt_9723485e19f163e8e518ca694e959cb9=1565142460,1566889728,1566971446,1566972223; Hm_lpvt_9723485e19f163e8e518ca694e959cb9=1567038980,DH_MM_ID=eznU711KLbp8pTYLA1RKAg==; _WX=vmmsu4mjicf8blgpg77k85d340; _csrf=01c2525a1051db91e8c684d82d3f0258114939aa86dc4e1aae65a5bca62ac23da^%^3A2^%^3A^%^7Bi^%^3A0^%^3Bs^%^3A5^%^3A^%^22_csrf^%^22^%^3Bi^%^3A1^%^3Bs^%^3A32^%^3A^%^22IQrvGkpRs8lbFuUR6KzY1RfFBtU9l91I^%^22^%^3B^%^7D; PHPSESSID=vdvhr8nvefo5f40369buufb8o3; Hm_lvt_74c7e2842e192eb6e87dd32cdcfcb60f=1566971446; Hm_lpvt_74c7e2842e192eb6e87dd32cdcfcb60f=1566971446; nb-referrer-hostname=www.iheima.com; nb-start-page-url=http^%^3A^%^2F^%^2Fwww.iheima.com^%^2Fcollege^%^2Fshiyanshi^%^3Ffm^%^3DBDSEM6^%^26renqun_youhua^%^3D1849731; BAIDU_SSP_lcr=https://www.baidu.com/link?url=bpMb4DLRHpTfxtAla5HqxHCBm_nlZ8Go4PVNnjQZVdi^&wd=^&eqid=db06facc002a5a06000000045d661935; Hm_lvt_9723485e19f163e8e518ca694e959cb9=1565142460,1566889728,1566971446,1566972223; Hm_lpvt_9723485e19f163e8e518ca694e959cb9=1567038980; DH_MM_ID=eznU711nHiOZMw6LBY1IAg==",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Referer': "http://www.iheima.com/enterprise-library/detail/75",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    'Postman-Token': "ce011ef2-a90f-4a31-9982-988ccc2bfe5a,2d504393-0bfb-44dc-be62-eae1aee3e782",
    'Host': "www.iheima.com",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
html = json.loads(response.text)
print(html)
