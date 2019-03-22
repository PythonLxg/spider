# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
# from scrapy.http.response.html import HtmlResponse


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://qiushibaike.com/text/page/2/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs:
            auth = duanzidiv.xpath(".//h2/text()").get().strip()  # 字符串
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()  # 列表
            content = ''.join(content).strip()  # 字符串
            # duanzi = {"auth": auth, "content": content}
            item = QsbkItem(auth=auth, content=content)
            yield item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url, callback=self.parse)
