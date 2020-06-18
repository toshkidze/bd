from urllib.parse import urljoin

import scrapy
from scrapy import Request


class DorogaSpider(scrapy.Spider):
    name = 'doroga'
    custom_settings = {
        'ITEM_PIPELINES': {
            'db_lab_1.pipelines.NewsXmlPipeline': 300,
        }
    }
    start_urls = [
        'http://www.doroga.ua/'
    ]
    allowed_domains = [
        'doroga.ua'
    ]

    def parse(self, response):
        text = filter(lambda x: x, [x.strip() for x in response.xpath('//*[not(self::script)]/text()').getall()])
        images = [urljoin(response.url, url) for url in response.xpath('//img[@src]/@src').getall()]
        yield {
            'text': text,
            'images': images,
            'url': response.url
        }
        for link_url in response.xpath('//a[@href]/@href').getall():
            try:
                yield Request(urljoin(response.url, link_url), callback=self.parse)
            except:
                pass
