# -*- coding: utf-8 -*-
import scrapy
from xici_agent.items import XiciAgentItem
from scrapy import Request

class XicispiderSpider(scrapy.Spider):
    name = 'xicispider'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        node_list = response.xpath(".//table[@id='ip_list']//tr[@class]")
        for node in node_list:
            item = XiciAgentItem()
            item['country'] = node.xpath("./td")[0].xpath("./img/@alt").extract_first()
            item['host'] = node.xpath("./td")[1].xpath("./text()").extract_first()
            item['port'] = node.xpath("./td")[2].xpath("./text()").extract_first()
            item['location'] = node.xpath("./td")[3].xpath("./a/text()").extract_first()
            item['is_nm'] = node.xpath("./td")[4].xpath("./text()").extract_first()
            item['types'] = node.xpath("./td")[5].xpath("./text()").extract_first()
            item['speed'] = node.xpath("./td")[6].xpath("./div[@class='bar']/@title").extract_first()
            item['conn_time'] = node.xpath("./td")[7].xpath("./div[@class='bar']/@title").extract_first()
            item['TTL'] = node.xpath("./td")[8].xpath("./text()").extract_first()
            item['check_time'] = node.xpath("./td")[9].xpath("./text()").extract_first()

            # 某记录的检查时间，年，月，日
            year = item['check_time'].split(' ')[0].split('-')[0]
            month = item['check_time'].split(' ')[0].split('-')[1]
            day = item['check_time'].split(' ')[0].split('-')[2]

            # 通过其检查时间来控制爬去的代理记录，太老旧的舍。
            if int(year) == 17 and int(month) == 8:
                yield item


        # 下一页，返回新的请求对象。
        if response.xpath(".//a[@class='next_page']"):
            next_url = response.xpath(".//a[@class='next_page']/@href").extract()[0]
            yield Request('http://www.xicidaili.com' + next_url, callback = self.parse)



        # pass
