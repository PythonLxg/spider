# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import requests


r = requests.get("https://www.baidu.com")  # 通过GET方式请求网页，返回一个Response对象
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# re1 = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")
print(type(r))
print(type(r.text))
print(r.text)
print(r.encoding)  # 默认ISO-8859-1
r.encoding = r.apparent_encoding  # 设置成网页表现的utf-8格式
print(type(r.status_code), r.status_code)
print(type(r.cookies), r.cookies)
print(type(r.headers), r.headers)
print("*" * 20)

r1 = requests.get("http://httpbin.org/get")
print(r1.text)

data = {
    'name': 'germey',
    'age': '22'
}
r3 = requests.get("http://httpbin.org/get", params=data)  # 附加额外信息,还有参数headers
print(r3.text)
print(r3.content)  # 爬取二进制数据，bytes类型
print(type(r3.text))  # str类型，JSON格式
print(r3.json())
print(type(r3.json()))  # dict类型
