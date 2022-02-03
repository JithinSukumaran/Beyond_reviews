import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books1'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    page_count = 0

    def parse(self, response):
        conts = response.xpath('//*[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]')

        for cont in conts:
            name = cont.xpath('.//img/@alt').extract()[0]
            cost = cont.xpath('.//*[@class= "price_color"]/text()').extract()[0]
            rating = cont.xpath('.//p/@class').extract()[0].split()[-1]

            yield {
			'Name':name,
			'Price':cost,
			'Star Rating':rating
			}

        next_page_url = response.xpath('//*[@class ="next"]/a/@href').extract()[0]
        absolute_next_page_url = response.urljoin(next_page_url)
        self.page_count +=1
        if self.page_count <=2:
            yield scrapy.Request(absolute_next_page_url)
