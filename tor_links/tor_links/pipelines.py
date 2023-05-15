# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

from elasticsearch import Elasticsearch
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TorLinksPipeline:
    def open_spider(self, spider):
        host = 'http://localhost:9200'
        self.eslastic = Elasticsearch(host)

    def process_item(self, item, spider):
        body = {
            "site_name": item.get("site_name"),
            "description": item.get("description"),
            "link": item.get("link"),
            "likes": item.get("likes"),
            "dislikes": item.get("dislikes"),
            "timestamp": datetime.now()}
        self.eslastic.index(index='scrapy_index', body=body)

    def close_spider(self, spider):
        self.eslastic.close()
