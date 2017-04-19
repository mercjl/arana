from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from pegasimporter.items import PegasimporterItem
from scrapy.spiders import CSVFeedSpider
from urlparse import urljoin


URL = "http://www.bne.cl/buscar-trabajo-empleo/?pagenumber=%d"

class MySpider(Spider):
    name = "bne"
    allowed_domains = ["bne.cl"]
    delimiter = ';'
    start_urls = [URL % 1]
    base = "http://www.bne.cl/"

    def __init__(self):
        self.page_number = 1

    def parse(self, response):
        print self.page_number
        print "----------"

        sel = Selector(response)
           

        for sel in response.xpath('.//div[@class="md2_oferta_content"]/div'):
            item = PegasimporterItem()
            item['cargo'] = map(unicode.strip, sel.xpath('//*[@id="avisosPortada"]/div[3]/table/tbody/tr[1]/td[2]/a/text()').extract())
            item['empresa'] = sel.xpath('//*[@id="avisosPortada"]/div[1]/table/tbody/tr[2]/td[3]/text()').extract()
            item['link'] = sel.xpath('//*[@id="avisosPortada"]/div[1]/table/tbody/tr[1]@href').extract()
            item['ciudad'] = sel.xpath('div[@class="sub_title"]/div[@class="lugarOferta"]/text()').extract()
            yield item
        self.page_number += 1
        yield Request(URL % self.page_number)











class TestSpider(CrawlSpider):
    name = 'bne'
    allowed_domains = ['bne.cl']
    delimiter = ';'
    start_urls = ['http://www.bne.cl/buscar-trabajo-empleo/?pagenumber=%s' % page for page in xrange(1,1500)]

    rules = (
        Rule(LinkExtractor(allow='/home/view\w*'), callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        
        item = PegasimporterItem()
        item['cargo'] = map(unicode.strip, response.xpath('//*[@id="avisoBNE"]/h1/text()').extract())
        item['empresa'] = map(unicode.strip, response.xpath('//*[@id="avisoBNE"]/div[1]/ul/li[1]/span[2]/a/text()').extract())
        item['link'] = response.url
        item['ciudad'] = map(unicode.strip, response.xpath('//*[@id="avisoBNE"]/div[5]/dl[2]/dd/text()').extract())
        item['fpublicacion'] = response.xpath('normalize-space(//*[@id="contenidoAviso"]/div[2]/table/tbody/tr[1]/td)').extract()
         

        yield item 
