# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from bson import ObjectId

from scrapy_crawl_example.settings import MONGODB_PORT, MONGODB_COLLECTION, MONGODB_DB, \
    MONGODB_HOST


class ScrapyCrawlExamplePipeline(object):
    def __init__(self):
        connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = connection[MONGODB_DB]
        self.collection = self.db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        self.collection.insert({"_id": str(ObjectId()),
                                'title': item['title'][0],
                                'description': item['description'][0]})
        return item
