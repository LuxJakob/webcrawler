from typing import Iterable

import scrapy
from prototypescraper.prototypescraper.items import PrototypeItem


class PrototypeSpider(scrapy.Spider):
    name = 'books'
    custom_settings = {
        'FEEDS': {'data.csv': {'format': 'csv', }}
    }

    def start_requests(self):
        url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css("div.product.main")

        prototype_item = PrototypeItem()
        prototype_item["title"] = product.css("h1 ::text").extract_first()
        prototype_item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").extract_first()
        prototype_item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()").extract_first()
        prototype_item['price'] = response.css('p.price_color ::text').extract_first()

        yield prototype_item
