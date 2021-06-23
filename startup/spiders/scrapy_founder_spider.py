import scrapy
from startup.items import Post

class ScrapyFounderSpiderSpider(scrapy.Spider):
    name = 'scrapy_founder_spider'
    allowed_domains = ['www.founder.co.jp']
    start_urls = ['https://www.founder.co.jp/']

    def parse(self, response):
        yield Post(title=response.css('title::text').get())
        for next_page in response.xpath('//a/@href').getall():
            if next_page is None:
                return
            yield scrapy.Request(next_page, callback=self.parse)
        
