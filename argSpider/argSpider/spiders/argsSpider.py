# -*- coding: utf-8 -*-
"""
语言版本：

python：3.6.1
scrapy：1.3.3

功能：本蜘蛛主要演示scrapy如何传参爬取
作者：cuanboy
出处：http://www.scrapyd.cn （scrapy中文网）
时间：2018年1月21日14:43:14
运行：CMD模式进入该项目目录（注意是argSpider下面，不是spider下面），若要爬取标签：”励志“下面的所有内容，可以输入如下命令：

scrapy crawl argsSpider -a tag=励志

若要爬取标签：爱情，可以输入：

scrapy crawl argsSpider -a tag=爱情

以此类推，爬取的数据最终会以文本的形式保存内容到argSpider目录下面

"""

import scrapy


class ArgsspiderSpider(scrapy.Spider):

    name = "argsSpider"

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容

    """
    以下内容为上一讲知识，若不清楚具体细节，请访问scrapy中文网（http://www.scrapyd.cn）
    查看scrapy文档：《scrapy爬取下一页》
    """

    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            text = v.css('.text::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            fileName = '%s-语录.txt' % tags
            with open(fileName, "a+") as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.write('\n-------\n')
                f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
