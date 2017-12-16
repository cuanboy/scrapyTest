"""
语言版本：

python：3.6.1
scrapy：1.3.3

功能：爬取http://lab.scrapyd.cn 里面的一条名言里的：名言内容、作者、标签，注意只是一条数据，然后保存为txt文档
作者：cuanboy
出处：http://www.scrapyd.cn （scrapy中文网）
时间：2017年12月16日15:55:00
运行：CMD模式进入项目目录，输入命令：scrapy crawl itemSpider

"""

import scrapy


class itemSpider(scrapy.Spider):
    name = 'itemSpider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote')[0]

        text = mingyan.css('.text::text').extract_first()  # 提取名言
        autor = mingyan.css('.author::text').extract_first()  # 提取作者
        tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
        tags = ','.join(tags)  # 数组转换为字符串

        fileName = '%s-语录.txt' % autor  # 爬取的内容存入文件，文件名为：作者-语录.txt
        f = open(fileName, "a+")  # 追加写入文件
        f.write(text)  # 写入名言内容
        f.write('\n')  # 换行
        f.write('标签：'+tags)  # 写入标签
        f.close()  # 关闭文件操作
