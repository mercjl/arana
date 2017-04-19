# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pegasimporter.items import PegasimporterItem
from scrapy.spiders import CSVFeedSpider
import string 


class TestSpider(CrawlSpider):
    name = 'computrabajo'
    allowed_domains = ['computrabajo.cl']
    delimiter = ','
    quotechar = '"'
    start_urls = ['http://www.computrabajo.cl/ofertas-de-trabajo/?p=%s' % page for page in xrange(1,500)]

    rules = (
        Rule(LinkExtractor(allow='/ofertas-de-trabajo/oferta-de-trabajo-de\w*'), callback='parse_item', follow=True),
    )   #/ofertas-de-trabajo/oferta-de-trabajo-de-operador-de-consola-windows-linux-7x24-lampa-en-santiago-providencia-BDEAFED64302A4DB



    def parse_item(self, response):
        
        item = PegasimporterItem()
        item['cargo'] = map(unicode.strip, response.xpath('//*[@id="MainContainer"]/article/header/h1/text()').extract())
        item['empresa'] = map(unicode.strip, response.xpath('//*[@id="MainContainer"]/article/section[5]/ul/li[1]/p/text()').extract())
        item['link'] = response.url
        item['ciudad'] = map(unicode.strip, response.xpath('//*[@id="MainContainer"]/article/section[5]/ul/li[6]/p/text()').extract())

        #//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span
        item['fpublicacion'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span)').extract()
         
          #response.xpath('concat(normalize-space(substring-before(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span, " ")),"-",normalize-space(substring-after(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span, " ")))')
          #response.xpath('normalize-space(substring-before(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span, " "))')
          #response.xpath('normalize-space(substring-after(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/p/span[2]/span, " "))')
        yield item 
