# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pegasimporter.items import PegasimporterItem
from scrapy.spiders import CSVFeedSpider
import string 
import hashlib


class TestSpider(CrawlSpider):
    name = 'trabajando2'
    allowed_domains = ['trabajando.cl']
    delimiter = ';'
    encoding='utf-8'
    start_urls = ['http://www.trabajando.cl/jobs/home/%s' % page for page in xrange(1,500)]

    rules = (
        Rule(LinkExtractor(allow='/empleos/ofertas/\d*/\w*.html'), callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        
        item = PegasimporterItem()
       
        item['cargo'] = map(unicode.strip, response.xpath('.//div[@class="titulo_oferta"]/h1/text()').extract())
        item['empresa'] = map(unicode.strip, response.xpath('.//div[@itemprop="hiringOrganization"]/a/text()').extract())
        
        if item['empresa']:
            print 'hola'
        else:
            item['empresa'] = map(unicode.strip, response.xpath('.//div[@itemprop="hiringOrganization"]/text()').extract())
            
        item['link'] = response.url
        item['ciudad'] = map(unicode.strip, response.xpath('.//div[@itemprop="jobLocation"]/text()').extract())
        item['fpublicacion'] = response.xpath('normalize-space(substring-after(.//div[@itemprop="datePosted"], "Publicado:"))').extract()
         

        yield item 
