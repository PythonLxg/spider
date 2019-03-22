# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import requests
from requests import Request, Session
from requests.packages import urllib3


# SSL证书检查
urllib3.disable_warnings()  # 忽略警告
response = requests.get('http://www.12306.cn', verify=False)  # verify表示不检查SSL证书，默认为True
print(response.status_code)

# 代理设置
# proxies = {
#     'http': 'http://user:password@10.10.1.10:3128/'
# }
# requests.get('http://www.taobao.com', proxies=proxies, timeout=1)  # timeout默认None，永远等待

# 身份认证
r = requests.get('https://github.com/PythonLxg', auth=('PythonLxg', 'lxg199661688'))
print(r.status_code)

# Prepared Requesr,将请求表示成数据结构
url = 'http://httpbin.org/post'
data = {
    'name': 'lxg'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/72.0.3626.96 Safari/537.36'
}

s = Session()
req = Request("POST", url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
