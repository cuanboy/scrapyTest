# SCRAPY爬虫实验

## mingyan2

mingyan2主要爬取 http://lab.scrapyd.cn 里面的两个页面并保存为html格式，其实就是一个下载的过程，目的很单纯，主要是让诸位理解scrapy是怎样爬起来的，里面需要神马内脏，大家可以下了运行试试！

## simpleStartUrl

scrapy初始url的两种写法

## itemSpider

此项目爬取 http://lab.scrapyd.cn 里面的一条名言里的：名言内容、作者、标签，注意只是一条数据，然后保存为txt文档，这个练习，主要是学习scrapy css选择器的基本用法，然后结合scrapy shell 进行相应调试

## listSpider

此项目爬取 http://lab.scrapyd.cn 首页的所有名言，也就是列表爬取，主要学习如何使用：
```
for …… in ……

```
这个循环方式进行递归爬取，快试试吧！
