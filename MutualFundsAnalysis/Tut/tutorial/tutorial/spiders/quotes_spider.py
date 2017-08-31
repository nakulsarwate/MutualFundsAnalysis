import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
	titles = response.selector.xpath("//div[@class='quote']")
        for quote in titles:
            yield {
                'text': quote.xpath('//span[@class="text"]/text()').extract_first(),
              #  'author': quote.xpath('//span/small[@class="author"]/text()').extract_first(),
                
            }
