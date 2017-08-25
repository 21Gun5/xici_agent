# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciAgentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host = scrapy.Field()
    port = scrapy.Field()
    country = scrapy.Field()
    location = scrapy.Field()
    types = scrapy.Field()
    speed = scrapy.Field()
    is_nm = scrapy.Field()
    conn_time = scrapy.Field()
    check_time = scrapy.Field()
    TTL = scrapy.Field()




    # //table[@id='ip_list']
    # pass
