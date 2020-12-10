import scrapy


class NewsItem(scrapy.Item):
    link_season = scrapy.Field()
    episodes = scrapy.Field()
