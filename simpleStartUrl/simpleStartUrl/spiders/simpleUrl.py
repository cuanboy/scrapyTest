"""
    初始链接的两种写法，
    一种是常量start_urls，并且需要定义一个方法parse（）
    另一种是直接定义一个方法：star_requests()
"""
import scrapy


class simpleUrl(scrapy.Spider):
    name = "simpleUrl"
    start_urls = [  #另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    # 另外一种初始链接写法
    # def start_requests(self):
    #     urls = [ #爬取的链接由此方法通过下面链接爬取页面
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    # 如果是简写初始url，此方法名必须为：parse


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
