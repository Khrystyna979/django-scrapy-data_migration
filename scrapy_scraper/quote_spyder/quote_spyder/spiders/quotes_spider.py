import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {"ITEM_PIPELINES": {"quote_spyder.pipelines.QuoteSpyderPipeline": 300}}
    
    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            item = QuoteItem()
            item['tags'] = quote.xpath('./div[@class="tags"]/a/text()').getall()
            item['author'] = quote.xpath('.//small[@class="author"]/text()').get()
            item['quote'] = quote.xpath('.//span[@class="text"]/text()').get()
            yield item
            
            author_link = quote.xpath('.//span/a/@href').get()
            if author_link:
                yield response.follow(author_link, callback=self.parse_authors)
                
        next_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link, callback=self.parse)
            
        
    def parse_authors(self, response):
        item = AuthorItem()
        item['fullname'] = response.xpath('//h3[@class="author-title"]/text()').get()
        item['born_date'] = response.xpath('//span[@class="author-born-date"]/text()').get()
        item['born_location'] = response.xpath('//span[@class="author-born-location"]/text()').get()
        item['description'] = response.xpath('//div[@class="author-description"]/text()').get().strip()
        yield item
                
