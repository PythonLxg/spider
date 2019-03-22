# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

r1 = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r1.content)

# 文件上传
files = {'file': open('favicon.ico', 'rb')}
r2 = requests.post('http://httpbin.org/post', files=files)
print(r2.text)
print("*"*20)

# 获取和设置Cookies
r3 = requests.get('https://www.baidu.com')
print(r3.cookies)
for key, value in r3.cookies.items():
    print(key + '=' + value)
print("*"*20)

# cookies = 'BAIDUID=46114143A55431F5B2DF3B052A7BCDD8:FG=1;' \
#           ' BIDUPSID=46114143A55431F5B2DF3B052A7BCDD8;' \
#           ' PSTM=1536109005; BD_UPN=12314753; ispeed_lsm=2;' \
#           ' BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0;' \
#           ' BD_HOME=0; H_PS_PSSID=1430_21092_28557_28607_28584_26350_28604_28627_20719;' \
#           ' BD_CK_SAM=1; PSINO=7'
# headers = {
#  'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                ' Chrome/72.0.3626.96 Safari/537.36'
# }

# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)

# r4 = requests.get('https://www.baidu.com', cookies=jar, heads=headers)
# print(r4.text)

# 会话维持
with requests.Session() as s:  # 维持同一个会话
    s.get('http://httpbin.org/cookies/set/number/123456')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
# 并不能获得cookies，因为不再同一个会话中
# requests.get('http://httpbin.org/cookies/set/number/123456')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
