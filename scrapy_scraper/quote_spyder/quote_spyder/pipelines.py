# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .items import QuoteItem, AuthorItem 
import json


class QuoteSpyderPipeline:
    quotes = []
    authors = []
    
    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            self.quotes.append(dict(item))
            return item
        elif isinstance(item, AuthorItem):
            self.authors.append(dict(item))
            return item
        
    
    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as fd:
            json.dump(self.quotes, fd, ensure_ascii=False, indent=4)
        with open('authors.json', 'w', encoding='utf-8') as fd:
            json.dump(self.authors, fd, ensure_ascii=False, indent=4)