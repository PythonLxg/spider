# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/21
import requests
from lxml import etree

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
# url = 'https://tieba.baidu.com/f?kw=美女&pn=250'


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input("请输入要爬取的贴吧的名字:")
        self.start_page = int(input('请输入起始页：'))
        self.end_page = int(input("请输入结束页："))
        self.url = "https://tieba.baidu.com/f?"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    def load_info(self, url_1):
        response = requests.get(url_1, headers=self.headers)
        return response

    @staticmethod
    def get_link_list(text, path):
        html = etree.HTML(text)
        link_list = html.xpath(path)
        return link_list

    def load_page(self, url_page):
        text = self.load_info(url_page).text
        link_list = self.get_link_list(text, '//div[@class="t_con cleafix"]/div[2]/div[1]/div[1]/a/@href')
        for link in link_list:
            full_link = "http://tieba.baidu.com" + link
            self.load_image(full_link)

    def write_image(self, link):
        image = self.load_info(link).content
        filename = image[-15:]
        with open('./imgs/' + filename, 'wb') as f:
            f.write(image)
        print("已经成功下载" + filename)

    def load_image(self, link):
        text = self.load_info(link).text
        link_list = self.get_link_list(text, '//img[@class="BDE_Image"]/@src')
        for link in link_list:
            if link.startswith("https://imgsa"):
                self.write_image(link)

    def load_tieba(self):
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50
            fullurl = self.url + f'kw={self.tieba_name}&pn={pn}'
            self.load_page(fullurl)
        print("感谢使用，再见")


if __name__ == "__main__":
    mySpider = TiebaSpider()
    mySpider.load_tieba()
