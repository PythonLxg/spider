# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WxappItem(scrapy.Item):
    title = scrapy.Field()
    auth = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()