import scrapy
from collections import Counter

class UfcSpider(scrapy.Spider):
    name = 'ufc'
    def start_requests(self):
        urls = [
            'https://www.ufc.com.br/rankings/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for pagina_atleta in response.css("#block-mainpagecontent a::attr('href')").getall():
            yield scrapy.Request(url="https://www.ufc.com.br"+pagina_atleta, callback=self.parseAtleta)

    def parseAtleta(self, response):
        i = response.css("h1::text").get()
        x=i.replace("\n","")
        y = x.strip()
        yield{
            'name': y,
            'idade': response.css(".field--type-integer::text").get(),
            'local': response.css(".c-bio__row--1col .c-bio__field--border-bottom-small-screens .c-bio__text::text").get(),
        }

