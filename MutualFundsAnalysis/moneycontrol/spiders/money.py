import scrapy
from moneycontrol.items import SampleItem

#class to crawl data about a mutual fund
class MoneySpider(scrapy.Spider):
    name = "money"    #name of our spider
    start_urls = [
        'http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/MBS104'    #url of the html page to scrape the data from 
    ]
 
    #function to parse the html page
    def parse(self, response):
	fund = response.selector.xpath('//div[@class="MT12 txtstrip"]')    #xpath selector to extract specific data    
	item = SampleItem()
	for f in fund:
		item['FundFamily'] = f.xpath("a/text()").extract_first()
		item['FundType'] = f.xpath("span/a/text()").extract_first()
		yield item    #store data in a key:value format
	
	item1 = SampleItem()
        money = response.selector.xpath('//table[@class="tblporhd"]/tr')
	for m in money:
                item1['Equity'] = m.xpath("td/a/text()").extract_first()
	        item1['Link'] = m.xpath("td/a/@href").extract_first()
		item1['Qty'] = m.xpath("td[@class='rgt']/text()").extract_first()
		item1['Value'] = m.xpath("(td[@class='rgt']/text())[2]").extract_first()
		item1['Percent'] = m.xpath("(td[@class='rgt']/text())[3]").extract_first()
		yield item1

#class to crawl the symbol of a mutual fund
class MF(scrapy.Spider):
    name = "mf"
    start_urls = [
        'http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/federalbank/FB'
    ]

    def parse(self, response):
	mf = response.selector.xpath('//div[@class="PB10"]')
	yield {
				'Symbol': mf.xpath('div/text()').extract()[1],
				
				}


#NOTE: The above program is hardcoded for only one website and a particular structure of an html page. The urls need to be changed for every mutual fund page displaying info about the stocks. Please visit the urls to get a clear picture and better understanding of the code.









