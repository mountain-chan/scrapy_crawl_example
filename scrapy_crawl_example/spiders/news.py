import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

from scrapy_crawl_example.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        urls = ['https://whatismyipaddress.com/']
        for url in urls:
            request = Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        ip = response.xpath("//*[@id='ipv4']/a/text()").extract_first()
        print("Your ip {}".format(ip))
        return
