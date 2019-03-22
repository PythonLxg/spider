# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import json


# loads()将JSON文本字符串转为JSON对象,list类型
# dumps()将JSON对象转为文本字符串
str1 = '''
[
    {
        "name": "Bob",
        "age": 23,
        "gender": "male"
    },
    {
        "name": "李小根",
        "age": 22,
        "gender": "男"
    }
]
'''
print(type(str1))  # JSON数据一定要用双引号
data = json.loads(str1)
print(type(data))
print(data)

# 写入json
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))

# 读取json
with open('data.json', 'r', encoding='utf-8') as f:
    content = f.read()
    data = json.loads(content)
    print(data)
