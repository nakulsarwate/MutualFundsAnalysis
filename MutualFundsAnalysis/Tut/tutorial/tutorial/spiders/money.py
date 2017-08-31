import scrapy
from tutorial.items import SampleItem

class MoneySpider(scrapy.Spider):
    name = "money"
    start_urls = [
        'http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/MBS104'
    ]

    def parse(self, response):
	fund = response.selector.xpath('//div[@class="MT12 txtstrip"]')
	item = SampleItem()
	for f in fund:
		item['FundFamily'] = f.xpath("a/text()").extract_first()
		item['FundType'] = f.xpath("span/a/text()").extract_first()
		yield item
	
	item1 = SampleItem()
        money = response.selector.xpath('//table[@class="tblporhd"]/tr')
	for m in money:
                item1['Equity'] = m.xpath("td/a/text()").extract_first()
	        item1['Link'] = m.xpath("td/a/@href").extract_first()
		item1['Qty'] = m.xpath("td[@class='rgt']/text()").extract_first()
		item1['Value'] = m.xpath("(td[@class='rgt']/text())[2]").extract_first()
		item1['Percent'] = m.xpath("(td[@class='rgt']/text())[3]").extract_first()
		yield item1

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












