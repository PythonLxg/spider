# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
from lxml import etree


text = """
<html><head><title>lixiaogen</title></head>
<p class='log'><span>--</span></div><div class="nav-name">娱乐</div></a><ul class="sub-nav"></p>
<li class="zy", name='zhongyi'><a href="//www.bilibili.com/v/ent/variety/"><span>综艺</span></a></li>
<li>
<a href="//www.bilibili.com/v/ent/star/"><span>明星</span></a></li><li>
<a href="//www.bilibili.com/v/ent/korea/"><span>Korea相关</span></a></li></ul></li>
<p id='href1'><li><a href="//www.bilibili.com/v/cinephile/">
<div class="num-wrap"><span>--</span></p></div>
<div class="nav-name">影视</div></a><ul class="sub-nav"><li>
<p><a href="//www.bilibili.com/v/cinephile/cinecism/"><span>影视杂谈</span></a></p>
</li>
<li><a href="//www.bilibili.com/v/cinephile/montage/"><span>影视剪辑</span></a></li>
<li><a href="//www.bilibili.com/v/cinephile/shortfilm/"><span>短片</span></a></li>
"""
html = etree.HTML(text)  # 构造一个Xpath解析对象
result = etree.tostring(html)  # 自动修正HTML文本，bytes类型
print(result.decode('utf-8'))  # 转换成str类型
print('*'*40)

# 也可以直接读取文本文件进行解析
html1 = etree.parse('./test.html', etree.HTMLParser())
result1 = etree.tostring(html1)
print(result1.decode('utf-8'))
print('*'*40)

# 所有节点
result2 = html1.xpath("//*")  # *代表获取所有节点,list类型
# result2 = html1.xpath("//*[@class=""]")[0].tag  # *代表获取属性class=""第一个节点的标签
result3 = html1.xpath('//li')  # 代表获取所有li节点
# result3 = html1.xpath('//li[last()-1]')  # 代表获取倒数第二个li节点
print(result2)
print(result3)
print(result3[0])  # 代表获取第一个li节点
print(result3[:2])  # 代表获取第一个li节点和第二个li节点

# 子节点
r1 = html1.xpath('//li/a')  # 选择li节点的所有直接a子节点
r2 = html1.xpath('//li//a')  # 选择li节点的所有a子孙节点
print(r1)
print(r2)

# 父节点
r3 = html1.xpath('//li/a[@href="//www.bilibili.com/v/ent/variety/"]/../@class')
# .表示当前节点，..表示父节点，@表示选取属性
print(r3)

# 文本获取
r3 = html1.xpath('//li/a[@href="//www.bilibili.com/v/ent/variety/"]/span/text()')
print(r3)

# 属性获取
r4 = html1.xpath('//li/a/@href')
# r4 = html1.xpath('//li/a/@class=""')[0].xpath(string(.))  获取所有内容除了标签
print(r4)

# 多属性匹配
r5 = html1.xpath('//li[@class="zy" and @name="zhongyi"]/a/span/text()')
print(r5)
