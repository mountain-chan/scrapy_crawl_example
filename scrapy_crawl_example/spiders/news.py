import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

from scrapy_crawl_example.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['https://vnexpress.net/thoi-su/chinh-tri']
    start_urls = ['https://vnexpress.net/thoi-su/chinh-tri/']

    def parse(self, response):
        yield Request(url='https://vnexpress.net/thoi-su/chinh-tri', callback=self.extract_news, dont_filter=True)

    def extract_news(self, response):
        for i in response.xpath('//article'):
            title = i.xpath('h2/a/text()').extract_first()
            description = i.xpath('p/a/text()').extract_first()

            loader = ItemLoader(item=NewsItem(), response=response)
            loader.add_value('title', title)
            loader.add_value('description', description)

            yield {
                "title": title,
                "description": description
            }
        next_page = response.xpath('//*[@id="pagination"]/div/a[5]/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.extract_news, dont_filter=True)
