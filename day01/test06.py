# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import csv
import pandas

# 写入
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=' ')  # 分隔符默认为，
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])  # writerow()写入一行数据
    writer.writerows([['10002', '李小根', '23'], ['10003', 'Jordan', '21']])  # writerows()写入多行数据

# with open('data.csv', 'w') as f:  # 添加字典类型的数据
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, delimiter=' ', fieldnames=fieldnames)
#     # writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Bob', 'age': '23'})

# 读取
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

df = pandas.read_csv('data.csv')
print(df)
