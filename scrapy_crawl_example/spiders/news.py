import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

from scrapy_crawl_example.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['https://www1.gowatchseries.bz/search.html?keyword=The%20Joy%20of%20Painting']
    start_urls = ['https://www1.gowatchseries.bz/search.html?keyword=The%20Joy%20of%20Painting']

    def parse(self, response):
        yield Request(url='https://www1.gowatchseries.bz/search.html?keyword=The%20Joy%20of%20Painting',
                      callback=self.extract_season, dont_filter=True)

    def extract_season(self, response):

        for i in response.xpath('//*[@id="left"]/div[3]/ul/li'):
            link_season = i.xpath('a/@href').extract_first()
            season_name = i.xpath('a/div[3]/text()').extract_first()

            if link_season:
                link_season = response.urljoin(link_season)
                yield scrapy.Request(url=link_season, callback=self.extract_episode, dont_filter=True)

    @staticmethod
    def extract_episode(response):
        list_episodes = []
        for i in response.xpath('//*[@id="left"]/div/div[3]/div[1]/div[3]/ul/li'):
            episode_name = i.xpath('a/text()').extract_first()
            link_episode = i.xpath('a/@href').extract_first()
            link_episode = response.urljoin(link_episode)
            item = {
                "episode_name": str(episode_name).strip(),
                "link_episode": link_episode
            }
            list_episodes.append(item)

        loader = ItemLoader(item=NewsItem(), response=response)
        loader.add_value('link_season', response.url)
        loader.add_value('episodes', list_episodes)

        yield loader.load_item()
