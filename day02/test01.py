# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python
# Author:李小根
# Time:2019/3/15
import re
import requests
import time


def get_page(url):
    """获取网页"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/72.0.3626.96 Safari/537.36'}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response
    return None


def parse_page(html):
    """提取信息"""
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">'
                         + '(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">'
                           '(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:],
            "time": item[4][5:],
            "score": item[5] + item[6]
        }


def write_page(content):
    with open("res.txt", "a", encoding="utf-8") as f:
        f.write(str(content) + "\n")


def main(offset_n):
    url = "https://maoyan.com/board/4?offset=" + str(offset_n)
    html = get_page(url).text

    for dianying in parse_page(html):
        print(dianying)
        write_page(dianying)
        item_image = get_page(dianying["image"]).content
        file_name = dianying["title"]
        with open("./images/" + f"{file_name}"+".png", "wb") as f:
            f.write(item_image)


if __name__ == "__main__":

    for i in range(10):
        offset = i * 10
        main(offset)
        time.sleep(1)
