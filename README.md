# scrapy-crawl-example
crawler website by scrapy in python

Environment: python 3.7

## create project scrapy
scrapy startproject scrapy-crawl-example

scrapy genspider news https://vnexpress.net/thoi-su/chinh-tri

scrapy shell https://vnexpress.net/thoi-su/chinh-tri

## Start crawl data
scrapy crawl news
