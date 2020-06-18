import os
from lxml import etree

os.system('scrapy crawl doroga')
with open('results/doroga.xml', 'r') as file:
    root = etree.parse(file)


def img_count(el):
    return int(el.xpath("count(./fragment[@type='image'])"))


pages = root.xpath('page')
page = min(pages, key=img_count)
page_url, img_count = page.xpath('./@url')[0], img_count(page)

print('Minimum images (%i) on page: %s' % (img_count, page_url))
