from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quote_spyder.spiders.quotes_spider import QuotesSpider
import seed

def run():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider)
    process.start() 

    print("Scraping finished. Starting data upload to MongoDB...")
    seed.load_data()
    print("All data successfully uploaded!")

if __name__ == '__main__':
    run()