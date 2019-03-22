# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/22
import requests
from lxml import etree


class QiubaiSpider(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/text/page/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        return response.text

    @staticmethod
    def parse_content(text):
        html = etree.HTML(text)
        item_info_list = html.xpath("//dic[@id='content-left']/div")
        for item_info in item_info_list:
            # 用户头像链接
            avatar = "http:" + item_info.xpath('./div[1]//img/@src')[0]
            # 作者
            auth = item_info.xpath('./div[1]//h2/text()')[0]
            # 内容
            content = item_info.xpath(".//div[@class='content']")[0].xpath('string(.)').strip()
            # 点赞
            star = item_info.xpath("./div[@class='stats']/span[1]/i/text()")[0]
            # 评论数
            comment_num = item_info.xpath("./div[@class='stats']/span[2]/a/i/text()")[0]
            yield {
                "auth": auth,
                "content": content,
                "star": star,
                "comment_num": comment_num,
                "avatar": avatar
            }

    @staticmethod
    def write_item(item, f):
        f.write(str(item) + '\n')

    def run(self):
        for page in range(1, 14):
            url = self.url + str(page)
            text = self.parse_page(url)
            items = self.parse_content(text)
            with open("qsbk.txt", "a", encoding='utf-8') as f:
                for item in items:
                    self.write_item(item, f)
            print(f"已爬取第{page}页")
        print("爬取完毕！")


if __name__ == "__main__":
    qiubai = QiubaiSpider()
    qiubai.run()
