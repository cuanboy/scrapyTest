# -*- coding: utf-8 -*-
import scrapy


class NextSpiderSpider(scrapy.Spider):
    name = "nextSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        pass
