import os
import lxml.etree as ET


def crawl():
    try:
        os.remove('results/freedelivery.xml')
    except OSError:
        print('results/freedelivery.xml not found')
    os.system('scrapy crawl freedelivery -o results/freedelivery.xml -t xml')


def xslt_parse():
    dom = ET.parse('results/freedelivery.xml')
    xslt = ET.parse('freedelivery.xslt')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    with open('results/freedelivery.html', 'wb') as f:
        f.write(ET.tostring(newdom, pretty_print=True))
    print('results/freedelivery.html was created')


crawl()
xslt_parse()
