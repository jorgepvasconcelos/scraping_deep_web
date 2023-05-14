# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from elasticsearch import Elasticsearch
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TorLinksPipeline:
    # def open_spider(self, spider):
    #     host = 'http://localhost:9200'
    #     self.eslastic = Elasticsearch(host)
    #
    def process_item(self, item, spider):
        print(item)
    #     line = json.dumps(ItemAdapter(item).asdict()) + "\n"
    #     self.file.write(line)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.eslastic.close()
