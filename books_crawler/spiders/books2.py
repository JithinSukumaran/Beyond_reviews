import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://http://books.toscrape.com//']

    def parse(self, response):
        pass
