# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pegasimporter.items import PegasimporterItem
from scrapy.spiders import CSVFeedSpider
import string 



class TestSpider(CrawlSpider):
    name = 'laborum33'
    allowed_domains = ['laborum.cl']
    delimiter = ';'
    start_urls = ['http://www.laborum.cl/empleos-pagina-%s.html' % page for page in xrange(1,500)]

    rules = (
        Rule(LinkExtractor(allow='/empleos/\w*'), callback='parse_item'), #, follow=True
    )



    def parse_item(self, response):
        
        item = PegasimporterItem()
        item['cargo'] = map(unicode.strip, response.xpath('.//*[@id="contenidoAviso"]/div[2]/div[2]/h2/text()').extract())
        item['empresa'] = map(unicode.strip, response.xpath('.//*[@id="contenidoAviso"]/div[2]/div[2]/h3/a/text()').extract())
        item['link'] = response.url
        item['ciudad'] = map(unicode.strip, response.xpath('.//*[@id="contenidoAviso"]/div[2]/table/tbody/tr[5]/td/a[1]/text()').extract())
        item['fpublicacion'] = response.xpath('.//*[@id="contenidoAviso"]/div[2]/table/tbody/tr[1]/td/text()').extract()
    

        yield item 
