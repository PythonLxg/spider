# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()  # 创建操作游标
cursor.execute('SELECT VERSION()')  # 游标执行sql语句
data = cursor.fetchone()  # 游标获取第一条数据
print('database version:', data)
cursor.execute('create database spiders default character set utf8')

# 创建表
sql = "create table if not exists students (id VARCHAR(255) NOT NULL," \
      " name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id)"
cursor.execute(sql)
db.close()


# 查询数据
sql1 = "select * from student where age >= 20"
try:
    cursor.execute(sql1)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Result:', results)
    print('Type of result:', type(results))
    for row in results:
        print(row)
except:
    print("Error")

# 更新数据
sql2 = 'update student set age=%s where name=%s'
try:
    cursor.execute(sql, (25, "Bob"))
    db.commit()
except:
    db.rollback()

db.close()

# 删除数据
table = 'students'
condition = "age>20"
sql3 = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execut(sql3)
    db.commit()
except:
    db.rollback()

db.close()


