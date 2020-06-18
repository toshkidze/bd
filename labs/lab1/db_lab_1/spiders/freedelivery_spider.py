from urllib.parse import urljoin

import scrapy


class FreeDeliverySpider(scrapy.Spider):
    name = "freedelivery"
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }
    start_urls = [
        'https://freedelivery.com.ua/dlya-3d-printerov-199/'
    ]
    allowed_domains = [
        'freedelivery.com.ua'
    ]

    def parse(self, response):
        for product in response.xpath('//div[@class="product-thumb thumbnail "]'):
            yield {
                'link': product.xpath('.//a/@href').get(),
                'price': product.xpath('normalize-space(.//p[@class="price"])').get(),
                'img': product.xpath('.//div[@class="image"]//img/@src').get(),
                'name': product.xpath('.//a/text()').get()
            }
